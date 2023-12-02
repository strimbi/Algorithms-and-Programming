from Domain.Getteri import get_destinatie, get_pret
from Utiles.Raportare.NumarOferteDestinatie import returneaza_numar_oferte_pentru_destinatie


#: 4.C
def returneaza_medie_de_pret_pentru_destinatie(lista_pachete, destinatie):
    medie = 0
    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if get_destinatie(pachet_curent) == destinatie:
            medie += get_pret(pachet_curent)
    numere = returneaza_numar_oferte_pentru_destinatie(lista_pachete, destinatie)
    return medie/numere
