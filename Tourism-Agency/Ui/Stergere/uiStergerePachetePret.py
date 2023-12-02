from Domain.Colors import TextFormatter
from Utiles.Stergere.StergerePachetePret import sterge_pachete_dupa_pret


# 2.C
def ui_sterge_pachete_dupa_pret(lista_pachete):
    pret = int(input("Input the maximum price wanted :"))
    return sterge_pachete_dupa_pret(lista_pachete, pret)
