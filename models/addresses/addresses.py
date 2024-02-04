


class Address:
    def __init__(self,
                 street_and_number: str,
                 postal_code: str,
                 city: str,
                 country: str = 'Hrvatska (Croatia)') -> None:
        self.street_and_number = street_and_number
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return (f'{self.street_and_number},\n'
                f'{self.postal_code} {self.city}, \n'
                f'{self.country}')
    