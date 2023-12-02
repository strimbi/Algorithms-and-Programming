from Utiles.Raportare.NumarOferteDestinatie import returneaza_numar_oferte_pentru_destinatie


'''
    Functia primeste parametrii introdusi de utilizatori in consola si printeaza numarul de pachete cu destinatie anume
 :param lista_pachete
 :param destinatie
 :param numar
 prints numar
'''


#: 4.A
def ui_tipareste_numar_oferte_pentru_destinatie(lista_pachete):
    destinatie = input("Input wanted destination :")
    numar = returneaza_numar_oferte_pentru_destinatie(lista_pachete, destinatie)
    print(numar)
