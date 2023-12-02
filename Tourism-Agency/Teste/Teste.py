from Domain.Getteri import get_zi_inceput, get_an_sfarsit
from Domain.Initi_Pachet import initializeaza_pachet
from Ui.ListaPachetePrecompletata import lista_pachete_precompletata
from Utiles.Cautare.PacheteDataSfarsit import returneaza_pachete_data_sfarsit
from Utiles.Cautare.PacheteIntervalDat import returneaza_pachet_interval_dat
from Utiles.Filtrare.StergePacheteDestinatiePret import sterge_pachet_destinatie_pret

'''
Aici testez diferite functii Utiles ale programului folosind functia assert
:param lista_pachete - lista pachetelor de calatorie
:param lista_corecta - lista cu care compar lista returnata de functia chemata
:param pachet_corect - pachetul corect pe care il introduc in lista corecta
:param zi_inceput
:param luna_inceput
:param an_inceput
:param zi_sfarsit
:param luna_sfarsit
:param an_sfarsit
:param destinatie
:param pret

'''

def teste():

    lista_corecta =[]
    pachet = initializeaza_pachet(10, 8, 2018, 24, 8, 2018, "Italy", 2080)
    assert get_zi_inceput(pachet) == 10
    assert get_an_sfarsit(pachet) == 2018

    lista_pachete = lista_pachete_precompletata()
    zi_sfarsit = 14
    luna_sfarsit = 8
    an_sfarsit = 2018
    lista_pachete_sfarsit = returneaza_pachete_data_sfarsit(lista_pachete, zi_sfarsit, luna_sfarsit, an_sfarsit)
    pachet_corect = initializeaza_pachet(9, 8, 2018, 14, 8, 2018, "Greece", 600)
    lista_corecta.append(pachet_corect)
    assert lista_pachete_sfarsit == lista_corecta

    lista_corecta =[]
    destinatie = "Greece"
    pret = 1000
    lista_pachete_destinatie = sterge_pachet_destinatie_pret(lista_pachete, destinatie, pret)
    pachet_corect = initializeaza_pachet(9, 8, 2018, 14, 8, 2018, "Greece", 600)
    lista_corecta.append(pachet_corect)
    assert lista_pachete_destinatie == lista_corecta

    lista_corecta =[]
    zi_inceput = 1
    luna_inceput = 8
    an_inceput = 2018
    zi_sfarsit = 26
    luna_sfarsit = 8
    an_sfarsit = 2018
    lista_interval = returneaza_pachet_interval_dat(lista_pachete, zi_inceput, luna_inceput, an_inceput, zi_sfarsit,
                                                    luna_sfarsit, an_sfarsit)
    pachet_corect = initializeaza_pachet(10, 8, 2018, 24, 8, 2018, "Italy", 2080)
    pachet_corect2 = initializeaza_pachet(9, 8, 2018, 14, 8, 2018, "Greece", 600)
    lista_corecta.append(pachet_corect)
    lista_corecta.append(pachet_corect2)
    assert lista_interval == lista_corecta
