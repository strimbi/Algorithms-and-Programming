from Domain.Getteri import get_luna_inceput, get_an_inceput, get_luna_sfarsit, get_an_sfarsit, get_zi_inceput, \
    get_zi_sfarsit


#: 2
def sterge_pachet_durata(lista_pachete, zile):

    lista_pachete_noua = []

    for pachet in lista_pachete:
        if get_an_inceput(pachet) > get_an_sfarsit(pachet):
            return 0
        else:
            if get_an_inceput(pachet) == get_an_sfarsit(pachet):
                if get_luna_inceput(pachet) == get_luna_sfarsit(pachet):
                    if get_zi_sfarsit(pachet) - get_zi_inceput(pachet) >= zile:
                        lista_pachete_noua.append(pachet)
                elif get_luna_inceput(pachet) > get_luna_sfarsit(pachet):
                    return 0
                elif get_zi_inceput(pachet) < get_zi_sfarsit(pachet):
                    zile_pachet = get_luna_sfarsit(pachet) * 31 - get_luna_inceput(pachet) * 31
                    zile_pachet = zile_pachet - get_zi_inceput(pachet) + 1 - 31 + get_zi_sfarsit(pachet)
                    for i in range(get_luna_inceput(pachet), get_luna_sfarsit(pachet)):
                        if (i % 2 == 0 and i <= 7) or (i % 2 == 1 and i >= 8):
                            zile_pachet = zile_pachet - 1
                    if zile_pachet >= zile:
                        lista_pachete_noua.append(pachet)
            else:
                if get_luna_inceput(pachet) == get_luna_sfarsit(pachet):
                    if get_zi_inceput(pachet) <= get_zi_sfarsit(pachet):
                        zile_pachet = 365 + get_zi_sfarsit(pachet) - get_zi_inceput(pachet)
                    else:
                        zile_pachet = 365 - (get_zi_inceput(pachet) - get_luna_sfarsit(pachet))
                    if zile_pachet >= zile:
                        lista_pachete_noua.append(pachet)
                elif get_luna_inceput(pachet) < get_luna_sfarsit(pachet):
                    zile_pachet = 365 + get_luna_sfarsit(pachet) * 31 - get_luna_inceput(pachet) * 31
                    zile_pachet = zile_pachet - get_zi_inceput(pachet) + 1 - 31 + get_zi_sfarsit(pachet)
                    for i in range(get_luna_inceput(pachet), get_luna_sfarsit(pachet)):
                        if (i % 2 == 0 and i <= 7) or (i % 2 == 1 and i >= 8):
                            zile_pachet = zile_pachet - 1
                    if zile_pachet >= zile:
                        lista_pachete_noua.append(pachet)
                elif get_luna_inceput(pachet) > get_luna_sfarsit(pachet):
                    zile_pachet = 365 + get_luna_inceput(pachet) * 31 - get_luna_sfarsit(pachet) * 31
                    zile_pachet = zile_pachet - get_zi_sfarsit(pachet) + 1 - 31 + get_zi_inceput(pachet)
                    for i in range(get_luna_sfarsit(pachet), get_luna_inceput(pachet)):
                        if (i % 2 == 0 and i <= 7) or (i % 2 == 1 and i >= 8):
                            zile_pachet = zile_pachet - 1
                    if zile_pachet >= zile:
                        lista_pachete_noua.append(pachet)

    return lista_pachete_noua
