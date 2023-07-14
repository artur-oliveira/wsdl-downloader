import abc
import os
from typing import List
from certificate import pfx_to_pem
from logger_utils import LoggerFactory
from models import WsdlImport

import requests

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass


class WsdlService(abc.ABC):
    def __init__(self, cert_path=None, cert_password=None):
        self.__cert_path = cert_path if cert_path else os.environ.get('CERT_PATH')
        self.__cert_password = cert_password if cert_password else os.environ.get('CERT_PASSWORD')
        self.__session = requests.Session()
        self.log = LoggerFactory.get_logger(self.__class__.__name__)

    def ssl_connection(self):
        return pfx_to_pem(self.__cert_path, self.__cert_password)

    def save_wsdl(self, cert, wsdl_url, wsdl_name):
        try:
            path = '/'.join([self.get_base_path(), wsdl_name])

            if os.path.exists(path):
                self.log.info(f'using cache for {wsdl_url}')
                return
            response = self.__session.get(url=wsdl_url, timeout=(1, 10), verify=False, cert=cert)

            response.raise_for_status()

            self.log.info(f'generated for {wsdl_url}')

            base_path = path[0:str(path).rindex('/')]
            if not os.path.exists(base_path):
                os.makedirs(base_path)

            with open(path, 'w') as f:
                f.write(response.text)
        except requests.exceptions.Timeout:
            self.log.error(f'timeout for {wsdl_url}')

    @abc.abstractmethod
    def get_wsdls(self) -> List[WsdlImport]:
        ...

    def run_import(self):
        with self.ssl_connection() as ssl_connection:
            for wsdl in self.get_wsdls():
                self.save_wsdl(cert=ssl_connection, wsdl_url=wsdl.wsdl_url, wsdl_name=wsdl.wsdl_name)

    @abc.abstractmethod
    def get_base_path(self) -> str:
        ...
