import time

from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form
from UI.components.console_components.create_customer_form import create_customer_form
from UI.components.console_components.create_employee_form import create_employee_form
from UI.components.console_components.select_contact_id_form import select_contact_id
from services.contact_services.contact_manager import ContactManager


def start_app():
    while True:
        main_menu()

        choice = int(input('Upisite broj iz izbornika: '))

        match choice:
            case 1:
                create_company_form()
            case 2:
                create_customer_form()
            case 3:
                create_employee_form()
            case 4:
                contact_manager = ContactManager()
                contacts = contact_manager.get_all()
                print(contacts)
                input('\nZa nastavak pritisnite tipku ENTER\n')
            case 5:
                contact_id = select_contact_id()
                contact_manager = ContactManager()
                contacts = contact_manager.get_contact(contact_id)
                if contacts != []:
                    print(contacts)
                else:
                    print('Nema trazenih informacija u bazi ili se dogodila greska')
                    #TODO provjera statusa greške pa prema tome ispisati predefiniranu grešku prema tipu statusa/greške
                    
                input('\nZa nastavak pritisnite tipku ENTER\n')

            case 0:
                return