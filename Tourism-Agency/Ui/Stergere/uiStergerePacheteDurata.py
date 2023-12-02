from Domain.Colors import TextFormatter
from Utiles.Stergere.StergerePacheteDurata import sterge_pachet_durata


def ui_stergere_pachete_durata(lista_pachete):
    zile = int(input("Input minimal day count wanted:"))
    if zile == 1 or zile == 0:
        print(f'{TextFormatter.RED_COL}This day count is not possible!'f'{TextFormatter.RESET}')
        return 0
    return sterge_pachet_durata(lista_pachete, zile)
