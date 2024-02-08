import os

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nPython Adresar')
    print('\t1. Kreiraj novu firmu')
    print('\t2. Kreiraj novog kupca')
    print('\t3. Kreiraj novog zaposlenika')
    print('\t4. Dohvati sve kontakte')
    print('\t5. Dohvati jedan kontakt')
    print('\t0. izlaz')