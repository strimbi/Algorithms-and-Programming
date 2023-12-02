from Domain.Colors import TextFormatter
from Domain.Initi_Pachet import initializeaza_pachet


'''
1.A
    In functia ui_adauga_pachet aplicatia primeste parametrii introdusi de catre utilizator ca dupa sa le transmita la 
functia initializaza_pachet, si adaugand pachetul nou creat in lista de pachete
    In plus folosesc clasa TextFormatter pentru printarea erorilor

:param lista_pachete - lista pachetelor de calatorie
:param zi_inceput
:param luna_inceput
:param an_inceput
:param zi_sfarsit
:param luna_sfarsit
:param an_sfarsit
:param destinatie
:param pret

'''


def ui_adauga_pachet(lista_pachete):

    zi_inceput = int(input("Input start day:"))
    if zi_inceput > 31 or zi_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another day.'f'{TextFormatter.RESET}'
        )
        return 0

    luna_inceput = int(input("Input start month:"))
    if luna_inceput > 12 or luna_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another month.'f'{TextFormatter.RESET}'
        )
        return 0

    an_inceput = int(input("Input start year:"))
    if an_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another year.'f'{TextFormatter.RESET}'
        )
        return 0

    zi_sfarsit = int(input("Input end day:"))
    if zi_sfarsit > 31 or zi_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another day.'f'{TextFormatter.RESET}'
        )
        return 0

    luna_sfarsit = int(input("Input end month:"))
    if luna_sfarsit > 12 or luna_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another month.'f'{TextFormatter.RESET}'
        )
        return 0

    an_sfarsit = int(input("Input start day:"))
    if an_sfarsit <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another year.'f'{TextFormatter.RESET}'
        )
        return 0

    destinatie = input("Input destination:")

    pret = int(input("Input price:"))
    if pret < 0:
        print(
            f'{TextFormatter.RED_COL}Price is not possible! Input another price.'f'{TextFormatter.RESET}'
        )
        return 0

    pachet = initializeaza_pachet(zi_inceput, luna_inceput, an_inceput, zi_sfarsit, luna_sfarsit, an_sfarsit,
                                  destinatie, pret)
    lista_pachete.append(pachet)
