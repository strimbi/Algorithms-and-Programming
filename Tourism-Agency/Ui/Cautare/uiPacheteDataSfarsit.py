from Domain.Colors import TextFormatter
from Ui.Tiparire import ui_tipareste_pachete
from Utiles.Cautare.PacheteDataSfarsit import returneaza_pachete_data_sfarsit


#: 2.C
def ui_pachete_data_sfarsit(lista_pachete):
    zi_sfarsit = int(input("Input end day wanted:"))
    if zi_sfarsit > 31 or zi_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another day.'f'{TextFormatter.RESET}'
        )
        return 0

    luna_sfarsit = int(input("Input end month wanted:"))
    if luna_sfarsit > 12 or luna_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another month.'f'{TextFormatter.RESET}'
        )
        return 0
    an_sfarsit = int(input("Input end year wanted:"))
    if an_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another year.'f'{TextFormatter.RESET}'
        )
        return 0

    lista_pachete = returneaza_pachete_data_sfarsit(lista_pachete, zi_sfarsit, luna_sfarsit, an_sfarsit)

    if len(lista_pachete) != 0:
        ui_tipareste_pachete(lista_pachete)
    else:
        print(f'{TextFormatter.YELLOW_COL}There are no packages of this type.'f'{TextFormatter.RESET}')
        return 0
