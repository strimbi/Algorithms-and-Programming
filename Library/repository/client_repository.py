from domain.Colors import X
from ui.listaprecompletata import lista_precompletata_clienti, lista_precompletata_clienti_inchiriere


class ClientRepository:

    def __init__(self):
        self.__lista_clienti = lista_precompletata_clienti()
        self.__lista_clienti_inchiriere = lista_precompletata_clienti_inchiriere()

    def get_all(self):
        return self.__lista_clienti

    def adauga(self, client):
        """
        Metoda care adauga un nou client in lista
        :param client:
        :return:
        Arunca o eroare daca id-ul clientului pe care vrem sa il introducem exista deja in lista. Eroarea e tratata
         in UI.
        """
        if self.gaseste_client_dupa_id(client.id) != -1:
            raise KeyError(X('\033[91m Exista deja o disciplina cu acest id! \033[0m'))
        else:
            self.__lista_clienti.append(client)

    def sterge(self, id_client):
        """
        Metoda care sterge un client din lista
        :param id_client:
        :return:
        Arunca o eroare daca id-ul clientului pe care vrem sa il stergem nu exista in lista. Eroarea e tratata in UI.
        """
        if self.gaseste_client_dupa_id(id_client) == -1:
            raise KeyError(X('\033[91m The client with this id does not exist! \033[0m'))
        else:
            index = self.gaseste_client_dupa_id(id_client)
            self.__lista_clienti.pop(index)

    def modifica(self, id_client, nume_nou, cnp_nou):
        """
        Metoda care modifica un client din lista
        :param id_client:
        :param nume_nou:
        :param cnp_nou:
        :return:
        Arunca o eroare daca id-ul clientului pe care vrem sa il modificam nu exista in lista. Eroarea e tratata in UI.
        """
        if self.gaseste_client_dupa_id(id_client) == -1:
            raise KeyError(X('\033[91m The client with this id does not exist!\033[0m'))
        else:
            index = self.gaseste_client_dupa_id(id_client)
            client = self.__lista_clienti[index]
            client.nume = nume_nou
            client.cnp = cnp_nou

    def gaseste_client_dupa_id(self, id_client):
        """
        Metoda care returneaza pozitia in lista de clienti al unui client, dupa id
        :param id_client:
        :return: pozitia clientului in lista, daca el exista in lista de clienti; -1, altfel
        """
        for i in range(0, len(self.__lista_clienti)):
            client_curent = self.__lista_clienti[i]
            if client_curent.id_client == id_client:
                return i
        return -1
