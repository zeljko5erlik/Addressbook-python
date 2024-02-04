from models.addresses.addresses import Address
from json import JSONEncoder


class Customer:
    def __init__(self,
                 name: str,
                 address: Address,
                 vat_id: str,
                 priority: str,
                 ) -> None:
        self.name = name
        self.address = address
        self.vat_id = vat_id
        self.priority = priority

    def __str__(self) -> str:
        return (f'Ime: {self.name},\n'
                f'Adresa: {self.address.__str__()},\n'
                f'OIB: {self.vat_id}\n'
                f'Prioritet: {self.priority}')
    

class CustomerEncoder(JSONEncoder):
    def default(self, cust_en):
        return cust_en.__dict__