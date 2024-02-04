from services.file_services.file_manager import FileManager
from UI.components.console_components.input_address_form import input_address_form

def create_customer_form():
    name = input('Upisite ime kupca: ')
    vat_id = input('Upisite OIB: ')
    priority = input('Upisite prioritet kupca: (high/medium/low)')
    address = input_address_form()

    file_mgr = FileManager()
    file_mgr.insert_customer(name, address, vat_id, priority)
