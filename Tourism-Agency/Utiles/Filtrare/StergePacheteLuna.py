from Domain.Getteri import get_luna_sfarsit, get_luna_inceput, get_an_inceput, get_an_sfarsit


'''
Functia creeaza o lista care contine pachetele fara luna primita prin param luna
:param lista_pachete - lista pachetelor de calatorie
:param luna

'''


#: 5.B
def sterge_pachet_luna(lista_pachete, luna):

    lista_pachete_noua = []

    for pachet in lista_pachete:
        if get_an_inceput(pachet) == get_an_sfarsit(pachet):
            if luna < get_luna_inceput(pachet) or luna > get_luna_sfarsit(pachet):
                lista_pachete_noua.append(pachet)
        elif get_an_sfarsit(pachet) - get_an_inceput(pachet) == 1 and get_luna_inceput(pachet) < \
                get_luna_sfarsit(pachet):
            lista_pachete_noua.append(pachet)

    return lista_pachete_noua
