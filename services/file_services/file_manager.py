import json
from models.companies.companies import Company


class FileManager:
    def __init__(self,
                 file_type: str = 'json',
                 file_path: str = 'files/companies.json') -> None:
        self.file_type = file_type
        self.file_path = file_path

    
    def insert_company(self, title, vat_id):

        company = Company(title, vat_id)

        try:
            with open(self.file_path, 'a') as file_writer:
                json.dump(company.__dict__, file_writer, indent=4)
                print(f'Uspjesno je kreirana firma {company}')
        
        except Exception as ex:
            print(f'Dogodila se greska {ex}')