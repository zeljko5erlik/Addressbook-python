import time

from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form
from UI.components.console_components.create_customer_form import create_customer_form
from UI.components.console_components.create_employee_form import create_employee_form


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
            case 0:
                return