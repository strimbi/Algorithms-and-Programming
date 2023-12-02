from Utiles.Cautare.PacheteIntervalDat import returneaza_pachet_interval_dat


'''
    Functia returneaza lista pachetelor dintr un anumit interval ordonate crescator
    :param lista_pachete
    :param zi_inceput
    :param luna_inceput
    :param an_inceput
    :param zi_sfarsit
    :param luna_sfarsit
    :param an_sfarsit
    :param destinatie
    :param pret
    :returns lista_pachete_noua_sortata
'''


def pachete_interval_timp_crescator(lista_pachete, zi_inceput, luna_inceput, an_inceput, zi_sfarsit,
                                    luna_sfarsit, an_sfarsit):

    lista_pachete_noua = returneaza_pachet_interval_dat(lista_pachete, zi_inceput, luna_inceput, an_inceput, zi_sfarsit,
                                                        luna_sfarsit, an_sfarsit)

    lista_pachete_noua_sortata = sorted(lista_pachete_noua, key=lambda x: x['pret'])

    return lista_pachete_noua_sortata
