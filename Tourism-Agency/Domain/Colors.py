"""
 Folosesc o clasa pentru a colora textele tiparite in consola in functie de:
 rosu - eroare a datelor introduse de utilizator
 galben - situatii in care nu este nimic de tiparit dupa comanda introdusa de utilizator

"""


class TextFormatter:

    # Blue colouring
    BLUE_COL = '\033[94m'
    # Red Colouring
    RED_COL = '\033[91m'
    # Green colouring
    GREEN_COL = '\033[92m'
    # Reset formatting and styling
    RESET = '\033[0m'
    # Yellow colouring
    YELLOW_COL = '\033[93m'
