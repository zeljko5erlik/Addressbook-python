import time

from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form


def start_app():
    while True:
        main_menu()

        choice = int(input('Upisite broj iz izbornika: '))

        match choice:
            case 1:
                create_company_form()
            case 2:
                pass
            case 3:
                pass
            case 0:
                return