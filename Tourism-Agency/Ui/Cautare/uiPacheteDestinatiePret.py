from Domain.Colors import TextFormatter
from Ui.Tiparire import ui_tipareste_pachete
from Utiles.Cautare.PacheteDestinatiePret import returneaza_pachet_destinatie_si_pret_mic


def ui_tipareste_pachet_destinatie_si_pret_mic(lista_pachete):
    destinatie = input("Input wanted destination :")
    pret = int(input("Input wanted price :"))
    lista_destinatie = returneaza_pachet_destinatie_si_pret_mic(lista_pachete, destinatie, pret)
    if len(lista_destinatie) != 0:
        ui_tipareste_pachete(lista_destinatie)
    else:
        print(f'{TextFormatter.YELLOW_COL}There are no packages of this type.'f'{TextFormatter.RESET}')
        return 0
