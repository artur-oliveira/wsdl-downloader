import json
from typing import List

from models import WsdlImport
from service import WsdlService


class AbstractNfceWsdlService(WsdlService):

    def __init__(self, cert_path, cert_password):
        super().__init__(cert_path, cert_password)
        with open('services/nfce_services.json') as f:
            self.services = json.load(f)

    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event_cancel.wsdl'),
            WsdlImport(self.event(), 'event_substitute_cancel.wsdl'),
            WsdlImport(self.authorization(), 'authorization.wsdl'),
            WsdlImport(self.inutilization(), 'inutilization.wsdl'),
            WsdlImport(self.query_protocol(), 'query_protocol.wsdl'),
            WsdlImport(self.return_authorization(), 'return_authorization.wsdl'),
            WsdlImport(self.status_service(), 'status_service.wsdl')
        ]
        return wsdl_import

    def _get_wsdl(self, name):
        return self.services.get(self.authorizer()).get(self.environment()).get(name)

    def event(self) -> str:
        return self._get_wsdl('event')

    def authorization(self) -> str:
        return self._get_wsdl('authorization')

    def inutilization(self) -> str:
        return self._get_wsdl('inutilization')

    def query_protocol(self) -> str:
        return self._get_wsdl('query_protocol')

    def return_authorization(self) -> str:
        return self._get_wsdl('return_authorization')

    def status_service(self) -> str:
        return self._get_wsdl('status_service')

    def authorizer(self) -> str:
        return self.__class__.__name__.lower().replace('nfce', '').replace(f'{self.environment()}wsdlservice', '')

    def environment(self) -> str:
        return 'prod' if 'prod' in self.__class__.__name__.lower() else 'hom'

    def get_base_path(self) -> str:
        return f'wsdl/nfce/{self.authorizer()}/{self.environment()}'


class NfceAmProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceAmHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceGoProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceGoHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceMgProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceMgHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceMsProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceMsHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceMtProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceMtHomWsdlService(AbstractNfceWsdlService):
    ...


class NfcePrProdWsdlService(AbstractNfceWsdlService):
    ...


class NfcePrHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceRsProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceRsHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceSpProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceSpHomWsdlService(AbstractNfceWsdlService):
    ...


class NfceSvrsProdWsdlService(AbstractNfceWsdlService):
    ...


class NfceSvrsHomWsdlService(AbstractNfceWsdlService):
    ...
