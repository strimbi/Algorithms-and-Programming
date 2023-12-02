from Domain.Getteri import get_destinatie, get_pret

'''

'''
#: 5.A

def sterge_pachet_destinatie_pret(lista_pachete, destinatie, pret):
    lista_pachete_noua = []
    for pachet in lista_pachete:
        if get_destinatie(pachet) == destinatie and get_pret(pachet) <= pret:
            lista_pachete_noua.append(pachet)

    return lista_pachete_noua
