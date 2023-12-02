from Domain.Getteri import get_destinatie, get_pret


#: 3.B
def returneaza_pachet_destinatie_si_pret_mic(lista_pachete, destinatie, pret):
    lista_pachete_destinatie = []
    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if get_destinatie(pachet_curent) == destinatie:
            if get_pret(pachet_curent) < pret:
                lista_pachete_destinatie.append(pachet_curent)
    return lista_pachete_destinatie
