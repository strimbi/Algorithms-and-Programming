from Domain.Colors import TextFormatter
from Ui.Tiparire import ui_tipareste_pachete
from Utiles.Raportare.PacheteIntervalTimpCrescator import pachete_interval_timp_crescator


def ui_pachete_interval_timp_crescator(lista_pachete):
    zi_inceput = int(input("Input start day wanted :"))
    if zi_inceput > 31 or zi_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another day.'f'{TextFormatter.RESET}'
        )
        return 0

    luna_inceput = int(input("Input start month wanted :"))
    if luna_inceput > 12 or luna_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another month.'f'{TextFormatter.RESET}'
        )
        return 0

    an_inceput = int(input("Input start year wanted :"))
    if an_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another year.'f'{TextFormatter.RESET}'
        )
        return 0

    zi_sfarsit = int(input("Input end day wanted :"))
    if zi_sfarsit > 31 or zi_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another day.'f'{TextFormatter.RESET}'
        )
        return 0

    luna_sfarsit = int(input("Input end month wanted :"))
    if luna_sfarsit > 12 or luna_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another month.'f'{TextFormatter.RESET}'
        )
        return 0

    an_sfarsit = int(input("Input end year wanted :"))
    if an_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another year.'f'{TextFormatter.RESET}'
        )
        return 0

    lista_pachete_noua = pachete_interval_timp_crescator(lista_pachete, zi_inceput, luna_inceput, an_inceput,
                                                         zi_sfarsit, luna_sfarsit, an_sfarsit)

    if len(lista_pachete_noua) != 0:
        ui_tipareste_pachete(lista_pachete_noua)
    else:
        print(f'{TextFormatter.YELLOW_COL} There are no packages of this type.'f'{TextFormatter.RESET}')
        return 0
