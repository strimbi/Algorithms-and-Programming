from Domain.Colors import TextFormatter
from Teste.Teste import teste
from Ui.Adaugare.uiAdaugaPachet import ui_adauga_pachet
from Ui.Adaugare.uiModificarePachet import ui_modifica_pachet
from Ui.Cautare.uiPacheteDataSfarsit import ui_pachete_data_sfarsit
from Ui.Cautare.uiPacheteDestinatiePret import ui_tipareste_pachet_destinatie_si_pret_mic
from Ui.Cautare.uiPacheteIntervalDat import ui_tipareste_pachet_interval_dat
from Ui.Filtrare.uiStergePacheteDestinatiePret import ui_sterge_pachet_destinatie_pret
from Ui.Filtrare.uiStergePacheteLuna import ui_sterge_pachete_luna
from Ui.ListaPachetePrecompletata import lista_pachete_precompletata
from Ui.Meniu import ui_meniu
from Ui.Raportare.uiMediePachetePretDestinatie import ui_tipareste_medie_de_pret_pentru_destinatie
from Ui.Raportare.uiNumarOferteDestinatie import ui_tipareste_numar_oferte_pentru_destinatie
from Ui.Raportare.uiPacheteIntervalTimp import ui_pachete_interval_timp_crescator
from Ui.Stergere.uiStergerePacheteDestinatie import ui_sterge_pachet_destinatie
from Ui.Stergere.uiStergerePacheteDurata import ui_stergere_pachete_durata
from Ui.Stergere.uiStergerePachetePret import ui_sterge_pachete_dupa_pret
from Ui.Tiparire import ui_tipareste_pachete
'''
    Enuntul:
        Creați o aplicație pentru gestiunea pachetelor de călătorie oferite de o agenție de
    turism. Aplicația stochează pachete de călătorie oferite clienților după cum
    urmează: data de început și cea de sfârșit a călătoriei, destinația și prețul.

'''

'''
    In functia aceasta se apeleaza functiile din UI si se da valori si listei undo pentru functia 15
    Importez majoritatea functiilor din UI, Utiles, Domain si Teste
    :param lista_pachete - lista pachetelor de calatorie
    :param zi_inceput   -start day
    :param luna_inceput -start month
    :param an_inceput   - start year
    :param zi_sfarsit   -end day
    :param luna_sfarsit -end month
    :param an_sfarsit   -end year
    :param destinatie   -destination
    :param pret -price
    
'''


def program():

    lista_undo = []
    lista_pachete = lista_pachete_precompletata()
    ruleaza = True
    while ruleaza == True:
        meniul_meu = ui_meniu()
        print(meniul_meu)
        comanda = input("Input command:")
        if comanda == "1":
            ui_tipareste_pachete(lista_pachete)
        elif comanda == "2":
            lista_undo = lista_pachete
            ui_adauga_pachet(lista_pachete)
        elif comanda == "3":
            lista_undo = lista_pachete
            lista_modifica = ui_modifica_pachet(lista_pachete)
            if lista_modifica != 0:
                lista_pachete = lista_modifica
        elif comanda == "4":
            lista_undo = lista_pachete
            lista_pachete = ui_sterge_pachet_destinatie(lista_pachete)
        elif comanda == "5":
            lista_undo = lista_pachete
            lista_durata = ui_stergere_pachete_durata(lista_pachete)
            if lista_durata != 0:
                lista_pachete = lista_durata
        elif comanda == "6":
            lista_undo = lista_pachete
            lista_pachete = ui_sterge_pachete_dupa_pret(lista_pachete)
        elif comanda == "7":
            ui_tipareste_pachet_interval_dat(lista_pachete)
        elif comanda == "8":
            ui_tipareste_pachet_destinatie_si_pret_mic(lista_pachete)
        elif comanda == "9":
            ui_pachete_data_sfarsit(lista_pachete)
        elif comanda == "10":
            ui_tipareste_numar_oferte_pentru_destinatie(lista_pachete)
        elif comanda == "11":
            ui_pachete_interval_timp_crescator(lista_pachete)
        elif comanda == "12":
            ui_tipareste_medie_de_pret_pentru_destinatie(lista_pachete)
        elif comanda == "13":
            lista_undo = lista_pachete
            lista_pachete = ui_sterge_pachet_destinatie_pret(lista_pachete)
        elif comanda == "14":
            lista_undo = lista_pachete
            lista_luna = ui_sterge_pachete_luna(lista_pachete)
            if lista_luna != 0:
                lista_pachete = lista_luna
        elif comanda == "15":
            lista_pachete = lista_undo
        elif comanda == "0":
            ruleaza = False
        else:
            print(f'{TextFormatter.RED_COL}Invalid command!'f'{TextFormatter.RESET}')


teste()
program()
