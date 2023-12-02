from domain.Colors import X
from domain.Numarinchirieri import Numarinchirieri
from ui.listaprecompletata import lista_precompletata_inchirieri, lista_precompletata_numar_inchirieri


class InchiriereRepository:

    def __init__(self, book_repository, client_repository):
        self.__lista_inchirieri = lista_precompletata_inchirieri()
        self.__numar_inchirieri = lista_precompletata_numar_inchirieri()
        self.__book_repository = book_repository
        self.__client_repository = client_repository

    def get_all_inchirieri(self):
        return self.__lista_inchirieri

    def get_all_numar(self):
        return self.__numar_inchirieri

    def inchiriere(self, inchiriere, id_carte, id_client):
        lista_clienti = self.__client_repository.get_all()
        self.__book_repository.lista_carti_inchiriate(id_carte)
        self.__lista_inchirieri.append(inchiriere)
        if len(self.__numar_inchirieri) == 0:
            index = self.__client_repository.gaseste_client_dupa_id(id_client)
            client = lista_clienti[index]
            nume = client.nume
            inchiriat = Numarinchirieri(id_client, 1, nume)
            self.__numar_inchirieri.append(inchiriat)
        else:
            ok = 0
            for inchi in self.__numar_inchirieri:
                if inchi.id_client == id_client:
                    numar = inchi.numar_carti
                    numar = numar + 1
                    inchi.numar_carti = numar
                    ok = 1
            if ok == 0:
                index = self.__client_repository.gaseste_client_dupa_id(id_client)
                client = lista_clienti[index]
                nume = client.get_nume()
                inchiriat = Numarinchirieri(id_client, 1, nume)
                self.__numar_inchirieri.append(inchiriat)

    def tipareste_cele_mai_inchiriate(self):
        lista_carti = []
        if len(self.__lista_inchirieri) == 0:
            raise KeyError(X('\033[93m There is no history of rented books! \033[0m'))
        else:
            max1 = 0
            id1 = 0
            max2 = 0
            id2 = 0
            for i in range(1, len(self.__lista_inchirieri)+1):
                suma = 0
                for carte in self.__lista_inchirieri:
                    if carte.id_carte == i:
                        suma = suma + 1
                if suma > max1:
                    max1 = suma
                    id1 = i
                elif suma >= max2:
                    max2 = suma
                    id2 = i
            lista_carti.append(self.__book_repository.afisare_carti(id1))
            lista_carti.append(self.__book_repository.afisare_carti(id2))
        return lista_carti

    def gaseste_pozitie(self, id_carte):
        for i in range(0, len(self.__lista_inchirieri)):
            carte_curenta = self.__lista_inchirieri[i]
            if carte_curenta.id_carte == id_carte:
                return i
        return -1

    def clienti_dupa_nume(self):
        lista_clienti = []
        if len(self.__numar_inchirieri) == 0:
            raise KeyError(X('\033[93m There is no history of rented books! \033[0m'))
        else:
            self.__numar_inchirieri.sort(key=lambda x: (x.nume, x.numar_carti))
            for inchi in self.__numar_inchirieri:
                lista_clienti.append(inchi)
        return lista_clienti

    def gaseste_pozitie_client(self, id_client):
        for i in range(0, len(self.__lista_inchirieri)):
            carte_curenta = self.__lista_inchirieri[i]
            if carte_curenta.id_client == id_client:
                return i
        return -1

    def returnare(self, id_client, id_carte):
        if self.gaseste_pozitie_client(id_client) == -1:
            raise KeyError(X('\033[93m Does not exist client with this id with rented books! \033[0m'))
        elif self.gaseste_pozitie(id_carte) == -1:
            raise KeyError(X('\033[93m Does not exist book rented with this id! \033[0m'))
        else:
            for carte in self.__lista_inchirieri:
                if id_client == carte.id_client:
                    if id_carte == carte.id_carte:
                        self.__book_repository.returnare_carte(id_carte)

    def cei_mai_activi_clienti(self):
        lista_clienti = []
        if len(self.__numar_inchirieri) == 0:
            raise KeyError(X('\033[93m There is no history of rented books! \033[0m'))
        else:
            self.__numar_inchirieri.sort(key=lambda x: x.numar_carti, reverse=True)
            lungime = len(self.__numar_inchirieri)
            lungime = int(0.2 * lungime)
            i = 0
            for inchi in self.__numar_inchirieri:
                if i <= lungime:
                    lista_clienti.append(inchi)
                    i = i + 1
                else:
                    break
        return lista_clienti
