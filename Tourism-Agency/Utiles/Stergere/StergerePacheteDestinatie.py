from Domain.Getteri import get_destinatie


#: 2.A
def sterge_pachet_destinatie(lista_pachete, destinatie):
    lista_pachete_noua = []
    for pachet in lista_pachete:
        if get_destinatie(pachet) != destinatie:
            lista_pachete_noua.append(pachet)

    lista_pachete = lista_pachete_noua
    return lista_pachete
