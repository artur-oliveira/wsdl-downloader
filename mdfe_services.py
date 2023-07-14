import json
from typing import List

from models import WsdlImport
from service import WsdlService


class AbstractMdfeWsdlService(WsdlService):

    def __init__(self, cert_path, cert_password):
        super().__init__(cert_path, cert_password)
        with open('services/mdfe_services.json') as f:
            self.services = json.load(f)

    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event.wsdl'),
            WsdlImport(self.reception(), 'reception.wsdl'),
            WsdlImport(self.return_reception(), 'return_reception.wsdl'),
            WsdlImport(self.reception_sync(), 'reception_sync.wsdl'),
            WsdlImport(self.query_situation(), 'query_situation.wsdl'),
            WsdlImport(self.query_unclosed(), 'query_unclosed.wsdl'),
            WsdlImport(self.distribution(), 'distribution.wsdl'),
            WsdlImport(self.status_service(), 'status_service.wsdl')
        ]
        return wsdl_import

    def _get_wsdl(self, name):
        authorizer = self.services.get(self.authorizer())
        environemnt = authorizer.get(self.environment())
        return environemnt.get(name)

    def query_situation(self) -> str:
        return self._get_wsdl('query_situation')

    def query_unclosed(self) -> str:
        return self._get_wsdl('query_unclosed')

    def distribution(self) -> str:
        return self._get_wsdl('distribution')

    def event(self) -> str:
        return self._get_wsdl('event')

    def reception_sync(self) -> str:
        return self._get_wsdl('reception_sync')

    def reception(self) -> str:
        return self._get_wsdl('reception')

    def return_reception(self) -> str:
        return self._get_wsdl('return_reception')

    def status_service(self) -> str:
        return self._get_wsdl('status_service')

    def authorizer(self) -> str:
        return self.__class__.__name__.lower().replace('mdfe', '').replace(f'{self.environment()}wsdlservice', '')

    def environment(self) -> str:
        return 'prod' if 'prod' in self.__class__.__name__.lower() else 'hom'

    def get_base_path(self) -> str:
        return f'wsdl/mdfe/{self.authorizer()}/{self.environment()}'


class MdfeSvrsProdWsdlService(AbstractMdfeWsdlService):
    ...


class MdfeSvrsHomWsdlService(AbstractMdfeWsdlService):
    ...
