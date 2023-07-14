import json
from typing import List

from models import WsdlImport
from service import WsdlService


class AbstractCteWsdlService(WsdlService):

    def __init__(self, cert_path, cert_password):
        super().__init__(cert_path, cert_password)
        with open('services/cte_services.json') as f:
            self.services = json.load(f)

    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event.wsdl'),
            WsdlImport(self.reception(), 'reception.wsdl'),
            WsdlImport(self.return_reception(), 'return_reception.wsdl'),
            WsdlImport(self.reception_os(), 'reception_os.wsdl'),
            WsdlImport(self.query_situation(), 'query_situation.wsdl'),
            WsdlImport(self.status_service(), 'status_service.wsdl')
        ]

        if self.reception_sync():
            wsdl_import.append(WsdlImport(self.reception_sync(), 'reception_sync.wsdl'))

        if self.reception_gtve():
            wsdl_import.append(WsdlImport(self.reception_gtve(), 'reception_gtve.wsdl'))

        return wsdl_import

    def _get_wsdl(self, name):
        authorizer = self.services.get(self.authorizer())
        environemnt = authorizer.get(self.environment())
        return environemnt.get(name)

    def query_situation(self) -> str:
        return self._get_wsdl('query_situation')

    def event(self) -> str:
        return self._get_wsdl('event')

    def reception_sync(self) -> str:
        return self._get_wsdl('reception_sync')

    def reception_os(self) -> str:
        return self._get_wsdl('reception_os')

    def reception(self) -> str:
        return self._get_wsdl('reception')

    def return_reception(self) -> str:
        return self._get_wsdl('return_reception')

    def reception_gtve(self) -> str:
        return self._get_wsdl('reception_gtve')

    def status_service(self) -> str:
        return self._get_wsdl('status_service')

    def authorizer(self) -> str:
        return self.__class__.__name__.lower().replace('cte', '').replace(f'{self.environment()}wsdlservice', '')

    def environment(self) -> str:
        return 'prod' if 'prod' in self.__class__.__name__.lower() else 'hom'

    def get_base_path(self) -> str:
        return f'wsdl/cte/{self.authorizer()}/{self.environment()}'


class CteAnProdWsdlService(AbstractCteWsdlService):
    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.distribution(), 'distribution.wsdl'),
        ]
        return wsdl_import

    def distribution(self) -> str:
        return self._get_wsdl('distribution')


class CteAnHomWsdlService(AbstractCteWsdlService):
    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.distribution(), 'distribution.wsdl'),
        ]
        return wsdl_import

    def distribution(self) -> str:
        return self._get_wsdl('distribution')


class CteMgProdWsdlService(AbstractCteWsdlService):
    ...


class CteMgHomWsdlService(AbstractCteWsdlService):
    ...


class CteMsProdWsdlService(AbstractCteWsdlService):
    ...


class CteMsHomWsdlService(AbstractCteWsdlService):
    ...


class CteMtProdWsdlService(AbstractCteWsdlService):
    ...


class CteMtHomWsdlService(AbstractCteWsdlService):
    ...


class CtePrProdWsdlService(AbstractCteWsdlService):
    ...


class CtePrHomWsdlService(AbstractCteWsdlService):
    ...


class CteSvspProdWsdlService(AbstractCteWsdlService):
    ...


class CteSvspHomWsdlService(AbstractCteWsdlService):
    ...


class CteSvrsProdWsdlService(AbstractCteWsdlService):
    ...


class CteSvrsHomWsdlService(AbstractCteWsdlService):
    ...
