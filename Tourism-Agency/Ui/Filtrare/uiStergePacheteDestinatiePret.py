from Utiles.Filtrare.StergePacheteDestinatiePret import sterge_pachet_destinatie_pret


def ui_sterge_pachet_destinatie_pret(listapachete):
    destinatie = input("Input wanted destination :")
    pret = int(input("Input maximal price wanted :"))
    return sterge_pachet_destinatie_pret(listapachete, destinatie, pret)
