from Domain.Getteri import get_zi_sfarsit, get_luna_sfarsit, get_an_sfarsit


'''
    Functia returneaza pachetele care au o anumita data de sfarsit
    :param lista_pachete - lista pachetelor de calatorie
    :param zi_sfarsit
    :param luna_sfarsit
    :param an_sfarsit
'''


def returneaza_pachete_data_sfarsit(lista_pachete, zi_sfarsit, luna_sfarsit, an_sfarsit):

    lista_pachete_sfarsit = []
    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if get_zi_sfarsit(pachet_curent) == zi_sfarsit and get_luna_sfarsit(pachet_curent) == luna_sfarsit \
                and get_an_sfarsit(pachet_curent) == an_sfarsit:
            lista_pachete_sfarsit.append(pachet_curent)

    return lista_pachete_sfarsit
