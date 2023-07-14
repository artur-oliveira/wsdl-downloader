import dataclasses


@dataclasses.dataclass
class WsdlImport:
    wsdl_url: str = dataclasses.field()
    wsdl_name: str = dataclasses.field()
