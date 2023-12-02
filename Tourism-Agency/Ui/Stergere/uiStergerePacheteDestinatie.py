from Utiles.Stergere.StergerePacheteDestinatie import sterge_pachet_destinatie


def ui_sterge_pachet_destinatie(lista_pachete):
    destinatie = input("Input wanted destination :")
    lista_pachete = sterge_pachet_destinatie(lista_pachete, destinatie)
    return lista_pachete
