from Domain.Getteri import get_zi_inceput, get_luna_inceput, get_an_inceput, get_zi_sfarsit, get_luna_sfarsit, \
    get_an_sfarsit, get_destinatie, get_pret


# in functia to_string(pachet) vom formata proprietatile pachetului
def to_string(pachet):
    string = ""
    string = string + "zi_inceput = " + get_zi_inceput(pachet) + "\n"
    string = string + "luna_inceput = " + get_luna_inceput(pachet) + "\n"
    string = string + "an_inceput = " + get_an_inceput(pachet) + "\n"
    string = string + "zi_sfarsit = " + get_zi_sfarsit(pachet) + "\n"
    string = string + "luna_sfarsit = " + get_luna_sfarsit(pachet) + "\n"
    string = string + "an_sfarsit = " + get_an_sfarsit(pachet) + "\n"
    string = string + "destinatie = " + str(get_destinatie(pachet)) + "\n"
    string = string + "pret = " + get_pret(pachet) + "\n"
    return string
