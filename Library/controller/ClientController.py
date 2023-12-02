from domain.Client import Client


class ClientController:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        """
        Metoda ce returneaza lista de obiecte din repository
        """
        return self.__repository.get_all()

    def adauga(self, id_client, nume, cnp):
        """
        Metoda ce adauga un student in lista (din repository)
        """
        client = Client(id_client, nume, cnp)
        self.__repository.adauga(client)

    def sterge(self, id_client):
        """
        Metoda care sterge un client din lista
        :param id_client:
        :return:
        """
        self.__repository.sterge(id_client)

    def cauta(self, id_client):
        """
        Metoda care cauta un client in lista
        :param id_client:
        :return:
        """
        index = self.__repository.gaseste_client_dupa_id(id_client)
        return index

    def modifica(self, id_client, nume_nou, cnp_nou):
        """
        Metoda care modifica datele unui client cu id-ul dat
        :param id_client:
        :param nume_nou:
        :param cnp_nou:
        """
        self.__repository.modifica(id_client, nume_nou, cnp_nou)
