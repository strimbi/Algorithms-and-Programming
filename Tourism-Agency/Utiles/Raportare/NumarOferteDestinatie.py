from Domain.Getteri import get_destinatie


#: 4.A
def returneaza_numar_oferte_pentru_destinatie(lista_pachete, destinatie):
    numar = 0
    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if get_destinatie(pachet_curent) == destinatie:
            numar += 1
    return numar
