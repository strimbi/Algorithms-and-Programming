from Domain.Getteri import get_zi_inceput, get_luna_inceput, get_an_inceput, get_zi_sfarsit, get_luna_sfarsit, \
    get_an_sfarsit


# 3.A
def returneaza_pachet_interval_dat(lista_pachete, zi_inceput, luna_inceput, an_inceput, zi_sfarsit,
                                   luna_sfarsit, an_sfarsit):
    lista_pachete_interval = []
    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if get_zi_inceput(pachet_curent) >= zi_inceput and get_luna_inceput(pachet_curent) >= luna_inceput \
                and get_an_inceput(pachet_curent) >= an_inceput:
            if get_zi_sfarsit(pachet_curent) <= zi_sfarsit and get_luna_sfarsit(pachet_curent) <= luna_sfarsit \
                    and get_an_sfarsit(pachet_curent) <= an_sfarsit:
                lista_pachete_interval.append(pachet_curent)
    return lista_pachete_interval
