from domain.Inchiriate import Inchiriate


class InchiriereController:

    def __init__(self, repository, book_repository, client_repository):
        self.__repository = repository
        self.__book_repository = book_repository
        self.__client_repository = client_repository

    def inchiriere_carte(self, id_client, id_carte):
        obiect = Inchiriate(id_client, id_carte)
        self.__repository.inchiriere(obiect, id_carte, id_client)

    def top_carti_inchiriate(self):
        return self.__repository.tipareste_cele_mai_inchiriate()

    def returnare_carte(self, id_client, id_carte):
        self.__repository.returnare(id_client, id_carte)

    def afisare_clienti_dupa_nume(self):
        return self.__repository.clienti_dupa_nume()

    def cei_mai_activi_clienti(self):
        return self.__repository.cei_mai_activi_clienti()
