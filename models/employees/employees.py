from models.addresses.addresses import Address
from json import JSONEncoder


class Employee:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 address: Address,
                 employee_no: int,
                 job_title: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.address = address	
        self.employee_no = employee_no
        self.job_title = job_title

    def __str__(self) -> str:
        return (f'Ime: {self.first_name}\n'
                f'Prezime: {self.last_name}\n'
                f'Osobni broj: {self.employee_no}\n'
                f'Radno mjesto: {self.job_title}')
    
    
class EmployeeEncoder(JSONEncoder):
    def default(self, empl_en):
        return empl_en.__dict__