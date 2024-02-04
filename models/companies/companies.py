from models.addresses.addresses import Address
from json import JSONEncoder


class Company:
    def __init__(self,
                 title: str,
                 vat_id: str,
                 hq_address: Address,
                 phone: str = None,
                 email: str = None) -> None:
        self.title = title
        self.vat_id = vat_id
        self.hq_address = hq_address
        self.phone = phone
        self.email = email
    
    def __str__(self) -> str:
        return (f'Naziv: {self.title},\n'
                f'OIB: {self.vat_id},\n'
                f'Sjediste: {self.hq_address.__str__()},\n'
                f'Telefon: {self.phone},\n'
                f'Email: {self.email}\n')
    

class CompanyEncoder(JSONEncoder):
    def default(self, comp_en):
        return comp_en.__dict__