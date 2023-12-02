from Domain.Initi_Pachet import initializeaza_pachet


'''
    Aici adaug pachete folosind functias append la lista de pachete
    :param lista_pachete - lista pachetelor de calatorie
    :returns lista_pachete - lista completata
'''


# aici initializam entitatile noastre din problema -> pachetul
def lista_pachete_precompletata():
    lista_pachete = []
    pachet1 = initializeaza_pachet(10, 8, 2018, 24, 8, 2018, "Italy", 2080)
    pachet2 = initializeaza_pachet(23, 9, 2019, 25, 9, 2019, "Cluj", 400)
    pachet3 = initializeaza_pachet(9, 8, 2018, 14, 8, 2018, "Greece", 600)
    pachet4 = initializeaza_pachet(14, 10, 2018, 30, 10, 2018, "Australia", 3050)
    pachet5 = initializeaza_pachet(28, 7, 2018, 4, 8, 2022, "Greece", 5000)
    pachet6 = initializeaza_pachet(10, 7, 2020, 15, 10, 2020, "Norway", 4060)
    pachet7 = initializeaza_pachet(28, 4, 2017, 3, 6, 2019, "Sicily", 2000)
    lista_pachete.append(pachet1)
    lista_pachete.append(pachet2)
    lista_pachete.append(pachet3)
    lista_pachete.append(pachet4)
    lista_pachete.append(pachet5)
    lista_pachete.append(pachet6)
    lista_pachete.append(pachet7)
    return lista_pachete
