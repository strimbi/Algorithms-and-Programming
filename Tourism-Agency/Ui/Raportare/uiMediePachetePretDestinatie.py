from Utiles.Raportare.MediePachetePretDestinatie import returneaza_medie_de_pret_pentru_destinatie


'''
 Functia primeste parametrii introdusi de utilizatori in consola si printeaza media de pret pentru pachete la aceeasi destinatie
 :param lista_pachete
 :param medie
 prints medie
'''


def ui_tipareste_medie_de_pret_pentru_destinatie(lista_pachete):
    destinatie = input("Input wanted destinaion :")
    medie = returneaza_medie_de_pret_pentru_destinatie(lista_pachete, destinatie)
    print(medie)
