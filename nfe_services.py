import json
from typing import List

from models import WsdlImport
from service import WsdlService


class AbstractNfeWsdlService(WsdlService):

    def __init__(self, cert_path, cert_password):
        super().__init__(cert_path, cert_password)
        with open('services/nfe_services.json') as f:
            self.services = json.load(f)

    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event_cancel.wsdl'),
            WsdlImport(self.event(), 'event_correction_letter.wsdl'),
            WsdlImport(self.authorization(), 'authorization.wsdl'),
            WsdlImport(self.inutilization(), 'inutilization.wsdl'),
            WsdlImport(self.query_protocol(), 'query_protocol.wsdl'),
            WsdlImport(self.return_authorization(), 'return_authorization.wsdl'),
            WsdlImport(self.status_service(), 'status_service.wsdl')
        ]

        if self.query_register():
            wsdl_import.append(
                WsdlImport(self.query_register(), 'query_register.wsdl')
            )
        return wsdl_import

    def _get_wsdl(self, name):
        authorizer = self.services.get(self.authorizer())
        environemnt = authorizer.get(self.environment())
        return environemnt.get(name)

    def query_register(self) -> str:
        return self._get_wsdl('query_register')

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
        return self.__class__.__name__.lower().replace('nfe', '').replace(f'{self.environment()}wsdlservice', '')

    def environment(self) -> str:
        return 'prod' if 'prod' in self.__class__.__name__.lower() else 'hom'

    def get_base_path(self) -> str:
        return f'wsdl/nfe/{self.authorizer()}/{self.environment()}'


class NfeAnProdWsdlService(AbstractNfeWsdlService):
    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event_epec.wsdl'),
            WsdlImport(self.event(), 'event_manifestation.wsdl'),
            WsdlImport(self.event(), 'event_interested_actor.wsdl'),
            WsdlImport(self.distribution(), 'distribution.wsdl'),
        ]
        return wsdl_import

    def distribution(self) -> str:
        return self._get_wsdl('distribution')


class NfeAnHomWsdlService(AbstractNfeWsdlService):
    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event_epec.wsdl'),
            WsdlImport(self.event(), 'event_manifestation.wsdl'),
            WsdlImport(self.event(), 'event_interested_actor.wsdl'),
            WsdlImport(self.distribution(), 'distribution.wsdl'),
        ]
        return wsdl_import

    def distribution(self) -> str:
        return self._get_wsdl('distribution')


class NfeAmProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeAmHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeBaProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeBaHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeGoProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeGoHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeMgProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeMgHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeMsProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeMsHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeMtProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeMtHomWsdlService(AbstractNfeWsdlService):
    ...


class NfePeProdWsdlService(AbstractNfeWsdlService):
    ...


class NfePeHomWsdlService(AbstractNfeWsdlService):
    ...


class NfePrProdWsdlService(AbstractNfeWsdlService):
    ...


class NfePrHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeRsProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeRsHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeSpProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeSpHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeSvanProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeSvanHomWsdlService(AbstractNfeWsdlService):
    ...


class NfeSvrsProdWsdlService(AbstractNfeWsdlService):
    ...


class NfeSvrsHomWsdlService(AbstractNfeWsdlService):
    ...
