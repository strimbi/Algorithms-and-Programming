from Domain.Colors import TextFormatter
from Utiles.Adaugare.ModificarePachet import modifica_pachet


'''
    In functie utilizatorul introduce in consola numarul pachetelui pe care vrea sa il modifice si datele necesare. 
    Functia apeleaza functia modifica_pachet din Utiles modificand pachetul dorit
    :param numar -- numarul pachetului
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


def ui_modifica_pachet(lista_pachete):

    numar = int(input("Input the package number which you want to modify:"))

    zi_inceput = int(input("Input start day wanted:"))
    if zi_inceput > 31 or zi_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another day.'f'{TextFormatter.RESET}'
        )
        return 0

    luna_inceput = int(input("Input start month wanted:"))
    if luna_inceput > 12 or luna_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another month.'f'{TextFormatter.RESET}'
        )
        return 0

    an_inceput = int(input("Input start year wanted:"))
    if an_inceput <= 0:
        print(
            f'{TextFormatter.RED_COL}Input date is not correct! Try another year.'f'{TextFormatter.RESET}'
        )
        return 0

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

    destinatie = input("Input destination:")

    pret = int(input("Input price:"))
    if pret < 0:
        print(
            f'{TextFormatter.RED_COL}This value is not possible! Input another price.'f'{TextFormatter.RESET}'
        )
        return 0

    return modifica_pachet(lista_pachete, zi_inceput, luna_inceput, an_inceput, zi_sfarsit, luna_sfarsit, an_sfarsit,
                           destinatie, pret, numar)
