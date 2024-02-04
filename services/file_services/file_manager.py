import json
from models.companies.companies import Company, CompanyEncoder
from models.customers.customers import Customer, CustomerEncoder
from models.employees.employees import Employee, EmployeeEncoder




class FileManager:
    def __init__(self,
                 file_type: str = 'json',
                 companies_file_path: str = 'files/companies.json',
                 customers_file_path: str = 'files/customers.json',
                 employees_file_path: str = 'files/employees.json') -> None:
        self.file_type = file_type
        self.companies_file_path = companies_file_path
        self.customers_file_path = customers_file_path
        self.employees_file_path = employees_file_path

    
    def insert_company(self, title, vat_id, hq_address):

        company = Company(title, vat_id, hq_address)

        try:
            with open(self.companies_file_path, 'a') as file_writer:
                json.dump(company, file_writer, indent=4, cls=CompanyEncoder)
                print(f'Uspjesno je kreirana tvrtka {company}')
                input()
        
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
            input('Za nastavak pritisnite ENTER!')

    
    def insert_customer(self, name, address, vat_id, priority):

        customer = Customer(name, address, vat_id, priority)

        try:
            with open(self.customers_file_path, 'a' ) as file_writer:
                json.dump(customer, file_writer, indent=4, cls=CustomerEncoder)
                print(f'Uspjesno je kreiran kupac: {customer}')
                input()
        
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
            input()


    def insert_employee(self, first_name, last_name, address, employee_no, job_title):

        employee = Employee(first_name, last_name, address, employee_no, job_title)

        try:
            with open(self.employees_file_path, 'a') as file_writer:
                json.dump(employee, file_writer, indent=4, cls=EmployeeEncoder)
                print(f'Uspjesno je kreiran zaposelnik: {employee}')
                input()

        except Exception as ex:
            print(f'Došlo je do greške {ex}')
            input()



