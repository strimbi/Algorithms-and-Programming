from domain.Colors import TextFormatter


class Console:

    def __init__(self, book_controller, client_controller, inchiriere_controller):
        self.__book_controller = book_controller
        self.__client_controller = client_controller
        self.__inchiriere_controller = inchiriere_controller

    def meniu(self):
        meniu = ""
        meniu += "1. Print all books\n"
        meniu += "2. Print all clients\n"
        meniu += "3. Search for book\n"
        meniu += "4. Search for client\n"
        meniu += "5. Add book\n"
        meniu += "6. Add client\n"
        meniu += "7. Delete book\n"
        meniu += "8. Delete client\n"
        meniu += "9. Modify book\n"
        meniu += "10. Modify client\n"
        meniu += "11. Rent book\n"
        meniu += "12. Return book\n"
        meniu += "13. Print most rented books\n"
        meniu += "14. Print clients with rented books\n"
        meniu += "15. Print the most active clients(20%)\n"
        meniu += "0. Exit\n"
        return meniu

    def program(self):
        ruleaza = True
        while ruleaza:
            meniul_meu = self.meniu()
            print(meniul_meu)
            comanda = input("Input command:")
            if comanda == "1":
                self.ui_tipareste_carti()
            elif comanda == "2":
                self.ui_tipareste_clienti()
            elif comanda == "3":
                self.ui_cautare_carte()
            elif comanda == "4":
                self.ui_cautare_client()
            elif comanda == "5":
                self.ui_adauga_carte()
            elif comanda == "6":
                self.ui_adauga_client()
            elif comanda == "7":
                self.ui_sterge_carte()
            elif comanda == "8":
                self.ui_sterge_client()
            elif comanda == "9":
                self.ui_modifica_carte()
            elif comanda == "10":
                self.ui_modifica_client()
            elif comanda == "11":
                self.ui_inchiriere_carte()
            elif comanda == "12":
                self.ui_returnare()
            elif comanda == "13":
                self.ui_afisare_cele_mai_inchiriate_carti()
            elif comanda == "14":
                self.ui_afisare_clienti_dupa_nume()
            elif comanda == "15":
                self.ui_cei_mai_activi()
            elif comanda == "0":
                ruleaza = False
            else:
                print(f'{TextFormatter.RED_COL}Command invalid! Retry!'f'{TextFormatter.RESET}')

    def ui_cautare_carte(self):

        id_carte = int(input("Input id:"))
        index = self.__book_controller.cauta(id_carte)
        carti = self.__book_controller.get_all()
        print(carti[index])

    def ui_cautare_client(self):
        id_client = int(input("Input id:"))
        index = self.__client_controller.cauta(id_client)
        clienti = self.__client_controller.get_all()
        print(clienti[index])

    def ui_adauga_carte(self):
        try:
            id_carte = int(input("Input id:"))
            titlu = input("Input title:")
            descriere = input("Input description:")
            autor = input("Input author:")
            self.__book_controller.add_fisier(id_carte, titlu, descriere, autor)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_adauga_client(self):
        try:
            id_client = int(input("Input id:"))
            nume = input("Input name:")
            cnp = input("Input cnp:")
            self.__client_controller.adauga(id_client, nume, cnp)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_tipareste_carti(self):
        carti = self.__book_controller.get_all()
        if len(carti) == 0:
            print(f'{TextFormatter.YELLOW_COL}List of books is empty!'f'{TextFormatter.RESET}')
        for carte in carti:
            print(carte)

    def ui_tipareste_clienti(self):
        clienti = self.__client_controller.get_all()
        if len(clienti) == 0:
            print(f'{TextFormatter.YELLOW_COL}List of clients is empty!'f'{TextFormatter.RESET}')
        for client in clienti:
            print(client)

    def ui_sterge_carte(self):
        try:
            id_carte = int(input("Input the books id which you want to delete:"))
            self.__book_controller.sterge(id_carte)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_sterge_client(self):
        try:
            id_client = int(input("Input the clients id which you want to delete:"))
            self.__client_controller.sterge(id_client)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_modifica_carte(self):
        try:
            id_carte = int(input("Input the books id which you want to modify:"))
            index = self.__book_controller.cauta(id_carte)
            carti = self.__book_controller.get_all()
            carte = carti[index]
            titlu_nou = carte.titlu
            descriere_noua = carte.descriere
            autor_nou = carte.autor
            modificari = int(input("How many elements do you want to modify? "))
            while modificari > 0:
                numar = input("Which ones? ")
                if numar == "title":
                    titlu_nou = input("Input new title:")
                elif numar == "description":
                    descriere_noua = input("Input new description:")
                elif numar == "author":
                    autor_nou = input("Input new author:")
                modificari = modificari - 1
            self.__book_controller.modifica(id_carte, titlu_nou, descriere_noua, autor_nou)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_modifica_client(self):
        try:
            id_client = int(input("Input the clients id which you want to modify:"))
            index = self.__client_controller.cauta(id_client)
            clienti = self.__client_controller.get_all()
            client = clienti[index]
            nume_nou = client.nume
            cnp_nou = client.cnp
            modificari = int(input("How many elements do you want to modify? "))
            while modificari > 0:
                numar = input("Which ones? ")
                if numar == "name":
                    nume_nou = input("Input new name:")
                elif numar == "cnp":
                    cnp_nou = int(input("Input new cnp:"))
                modificari = modificari - 1
            self.__client_controller.modifica(id_client, nume_nou, cnp_nou)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_inchiriere_carte(self):
        try:
            id_client = int(input("Input client id:"))
            id_carte = int(input("Input id of book which you want to rent:"))
            self.__inchiriere_controller.inchiriere_carte(id_client, id_carte)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_afisare_cele_mai_inchiriate_carti(self):
        try:
            lista = self.__inchiriere_controller.top_carti_inchiriate()
            for carte in lista:
                print(carte)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_returnare(self):
        try:
            id_client = int(input("Input client id:"))
            id_carte = int(input("Input id of book which you want to return:"))
            self.__inchiriere_controller.returnare_carte(id_client, id_carte)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_afisare_clienti_dupa_nume(self):
        try:
            lista = self.__inchiriere_controller.afisare_clienti_dupa_nume()
            for carte in lista:
                print(carte)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)

    def ui_cei_mai_activi(self):
        try:
            lista = self.__inchiriere_controller.cei_mai_activi_clienti()
            for carte in lista:
                print(carte)
        except ValueError:
            print(f'{TextFormatter.RED_COL}Wrong data! Retry!'f'{TextFormatter.RESET}')
        except KeyError as ke:
            print(ke)
