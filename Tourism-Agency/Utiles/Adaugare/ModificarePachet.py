from Domain.Setteri import set_destinatie, set_pret, set_zi_inceput, \
    set_luna_inceput, set_an_inceput, set_zi_sfarsit, set_luna_sfarsit, set_an_sfarsit


# 1.B
def modifica_pachet(lista_pachete, zi_inceput_noua, luna_inceput_noua, an_inceput_nou, zi_sfarsit_noua,
                    luna_sfarsit_noua, an_sfarsit_nou, destinatie_noua, pret_nou, numar):

    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if i == numar - 1:
            set_zi_inceput(pachet_curent, zi_inceput_noua)
            set_luna_inceput(pachet_curent, luna_inceput_noua)
            set_an_inceput(pachet_curent, an_inceput_nou)
            set_zi_sfarsit(pachet_curent, zi_sfarsit_noua)
            set_luna_sfarsit(pachet_curent, luna_sfarsit_noua)
            set_an_sfarsit(pachet_curent, an_sfarsit_nou)
            set_destinatie(pachet_curent, destinatie_noua)
            set_pret(pachet_curent, pret_nou)

    return lista_pachete
