"""
    In functia initializeaza_pachet adaugam pachetele cu valorile transmise ca parametrii in dictionarul nostru,
 dictionar pachet.
 :param zi_inceput
 :parameter luna_inceput
 :param an_inceput
 :param zi_sfarsit
 :param luna_sfarsit
 :param an_sfarsit
 :param destinatie
 :param pret
 :returns dictionar_pachet -- dictionarul continand pachetele de calatorie
"""


def initializeaza_pachet(zi_inceput, luna_inceput, an_inceput, zi_sfarsit, luna_sfarsit, an_sfarsit, destinatie, pret):
    dictionar_pachet = {"zi_inceput": zi_inceput, "luna_inceput": luna_inceput, "an_inceput": an_inceput,
                        "zi_sfarsit": zi_sfarsit, "luna_sfarsit": luna_sfarsit, "an_sfarsit": an_sfarsit,
                        "destinatie": destinatie, "pret": pret}
    return dictionar_pachet
