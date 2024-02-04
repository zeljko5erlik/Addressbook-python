from models.addresses.addresses import Address

def input_address_form():
    street_and_number = input('Upisite ulicu i kucni broj: ')
    postal_code = input('Upisite broj postanskog ureda: ')
    city = input('Upisite grad: ')
    country = input('Upisite drzavu: ')

    input_adress = Address(street_and_number, postal_code, city, country)

    return input_adress