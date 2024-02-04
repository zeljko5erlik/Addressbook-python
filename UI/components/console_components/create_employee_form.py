from services.file_services.file_manager import FileManager
from UI.components.console_components.input_address_form import input_address_form


def create_employee_form():
    employee_no = input('Unesite osobni broj: ')
    first_name = input('Unesite ime: ')
    last_name = input('Unesite prezime: ')
    job_title = input('Unesite radno mjesto: ')
    address = input_address_form()

    file_mgr = FileManager
    file_mgr.insert_employee(first_name, last_name, address, employee_no, job_title)
