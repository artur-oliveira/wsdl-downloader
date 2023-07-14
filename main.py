import urllib3

from cte4_services import AbstractCte4WsdlService
from cte_services import AbstractCteWsdlService
from mdfe_services import AbstractMdfeWsdlService
from nfce_services import AbstractNfceWsdlService
from nfe_services import AbstractNfeWsdlService

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    classes = []
    classes.extend(AbstractNfeWsdlService.__subclasses__())
    classes.extend(AbstractNfceWsdlService.__subclasses__())
    classes.extend(AbstractCte4WsdlService.__subclasses__())
    classes.extend(AbstractCteWsdlService.__subclasses__())
    classes.extend(AbstractMdfeWsdlService.__subclasses__())

    for cls in classes:
        cls(
            cert_path='/home/artur/Documents/Certificates/11520224000140.pfx',
            cert_password='2023@revgas'
        ).run_import()
