from Domain.Colors import TextFormatter
from Utiles.Filtrare.StergePacheteLuna import sterge_pachet_luna

'''
    In functia aceasta utilizatorul introduce luna dorita si functia apeleaza functia sterge pachete luna
    :param lista_pachete - lista pachetelor de calatorie
    :param luna

'''


def ui_sterge_pachete_luna(lista_pachete):

    luna = int(input("Input month: "))

    if luna <= 0 or luna > 12:
        print(f'{TextFormatter.RED_COL}This month does not exist!'f'{TextFormatter.RESET}')
        return 0
    else:
        return sterge_pachet_luna(lista_pachete, luna)
