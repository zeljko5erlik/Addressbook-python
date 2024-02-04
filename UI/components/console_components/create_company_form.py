from services.file_services.file_manager import FileManager
from UI.components.console_components.input_address_form import input_address_form


def create_company_form():
    title = input('Upisite naziv tvrtke: ')
    vat_id = input('Upisite OIB tvrtke: ')
    hq_address = input_address_form()

    file_mgr = FileManager()
    file_mgr.insert_company(title, vat_id, hq_address)