import requests
from services.file_services.logging_manager import LoggingManager
from commons.app_constants import BASE_URL, LOG_ERROR, LOG_INFO, LOG_WARNING
from commons.message_generator import generate_log_message

class ContactManager:
    def __init__(self,
                 base_url: str = BASE_URL,
                 contacts_url: str = '/users') -> None:
        self.base_url: str = base_url
        self.contacts_url: str = contacts_url


    def get_all(self):
        try:
            response = requests.get(f'{self.base_url}{self.contacts_url}')
            if response.status_code == 200:
                return response.json()
            else:
                return[]
        except Exception as ex:
            logger = LoggingManager()
            message = generate_log_message(ex, LOG_ERROR)
            logger.save_message(message)
            return []
        
    def get_contact(self, contact_id: int):
        try:
            response = requests.get(f'{self.base_url}{self.contacts_url}/{contact_id}')
            if response.status_code == 200:
                return response.json()
            else:
                return[]
        except Exception as ex:
            logger = LoggingManager()
            message = generate_log_message(ex, LOG_ERROR)
            logger.save_message(message)
            return []
