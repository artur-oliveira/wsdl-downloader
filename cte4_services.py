import json
from typing import List

from models import WsdlImport
from service import WsdlService


class AbstractCte4WsdlService(WsdlService):

    def __init__(self, cert_path, cert_password):
        super().__init__(cert_path, cert_password)
        with open('services/cte4_services.json') as f:
            self.services = json.load(f)

    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.event(), 'event.wsdl'),
            WsdlImport(self.reception_sync(), 'reception_sync.wsdl'),
            WsdlImport(self.reception_os(), 'reception_os.wsdl'),
            WsdlImport(self.reception_gtve(), 'reception_gtve.wsdl'),
            WsdlImport(self.query_situation(), 'query_situation.wsdl'),
            WsdlImport(self.status_service(), 'status_service.wsdl')
        ]
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

    def reception_gtve(self) -> str:
        return self._get_wsdl('reception_gtve')

    def status_service(self) -> str:
        return self._get_wsdl('status_service')

    def authorizer(self) -> str:
        return self.__class__.__name__.lower().replace('cte4', '').replace(f'{self.environment()}wsdlservice', '')

    def environment(self) -> str:
        return 'prod' if 'prod' in self.__class__.__name__.lower() else 'hom'

    def get_base_path(self) -> str:
        return f'wsdl/cte4/{self.authorizer()}/{self.environment()}'


class Cte4AnProdWsdlService(AbstractCte4WsdlService):
    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.distribution(), 'distribution.wsdl'),
        ]
        return wsdl_import

    def distribution(self) -> str:
        return self._get_wsdl('distribution')


class Cte4AnHomWsdlService(AbstractCte4WsdlService):
    def get_wsdls(self) -> List[WsdlImport]:
        wsdl_import = [
            WsdlImport(self.distribution(), 'distribution.wsdl'),
        ]
        return wsdl_import

    def distribution(self) -> str:
        return self._get_wsdl('distribution')


class Cte4MgProdWsdlService(AbstractCte4WsdlService):
    ...


class Cte4MgHomWsdlService(AbstractCte4WsdlService):
    ...


class Cte4MsProdWsdlService(AbstractCte4WsdlService):
    ...


class Cte4MsHomWsdlService(AbstractCte4WsdlService):
    ...


class Cte4MtProdWsdlService(AbstractCte4WsdlService):
    ...


class Cte4MtHomWsdlService(AbstractCte4WsdlService):
    ...


class Cte4PrProdWsdlService(AbstractCte4WsdlService):
    ...


class Cte4PrHomWsdlService(AbstractCte4WsdlService):
    ...


class Cte4SvspProdWsdlService(AbstractCte4WsdlService):
    ...


class Cte4SvspHomWsdlService(AbstractCte4WsdlService):
    ...


class Cte4SvrsProdWsdlService(AbstractCte4WsdlService):
    ...


class Cte4SvrsHomWsdlService(AbstractCte4WsdlService):
    ...
