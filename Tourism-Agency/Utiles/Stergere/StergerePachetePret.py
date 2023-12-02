from Domain.Getteri import get_pret


def sterge_pachete_dupa_pret(lista_pachete, pret):

    lista_pachete_noua = []
    for pachet in lista_pachete:
        if get_pret(pachet) <= pret:
            lista_pachete_noua.append(pachet)

    lista_pachete = lista_pachete_noua
    return lista_pachete
