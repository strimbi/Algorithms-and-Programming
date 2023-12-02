from Domain.Colors import TextFormatter
from Domain.Getteri import get_zi_inceput, get_luna_inceput, get_an_inceput, get_pret, get_zi_sfarsit, get_destinatie, \
    get_luna_sfarsit


#: 1.0
def ui_tipareste_pachete(lista_pachete):
    if len(lista_pachete) == 0:
        print(f'{TextFormatter.YELLOW_COL}List of packages is empty!'f'{TextFormatter.RESET}')
    for i in range(0, len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        print("Start date:", get_zi_inceput(pachet_curent), "/", get_luna_inceput(pachet_curent), "/", get_an_inceput
              (pachet_curent), ";", "End date:", get_zi_sfarsit(pachet_curent), "/",
              get_luna_sfarsit(pachet_curent), "/", get_an_inceput(pachet_curent), ";", "Destination:",
              get_destinatie(pachet_curent), ";", "Price:", get_pret(pachet_curent))
