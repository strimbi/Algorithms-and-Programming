from domain.Book import Book


class BookController:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        """
        Metoda ce returneaza lista de obiecte din repository
        :return: lista de obiecte din repository
        """
        return self.__repository.get_all()

    def get_all_inchiriate(self):
        """
        Metoda ce returneaza lista de obiecte din repository
        :return: lista de obiecte din repository
        """
        return self.__repository.get_all_inchiriate()

    def adauga(self, id_book, titlu, descriere, autor):
        """
        Metoda ce adauga un student in lista
        :param id_book:
        :param titlu:
        :param descriere:
         :param autor:
        """
        book = Book(id_book, titlu, descriere, autor)
        self.__repository.adauga(book)

    def add_fisier(self, id_book, titlu, descriere, autor):
        """
        Metoda ce adauga un student in lista
        :param id_book:
        :param titlu:
        :param descriere:
         :param autor:
        """
        self.__repository.add_fisier(id_book, titlu, descriere, autor)

    def sterge(self, id_carte):
        """
        Metoda care sterge o carte din lista (din repository)
        :param id_carte:
        :return:
        """
        self.__repository.sterge(id_carte)

    def cauta(self, id_carte):
        """
        Metoda care sterge o carte din lista (din repository)
        :param id_carte:truj y
        :return:
        """
        index = self.__repository.gaseste_carte_dupa_id(id_carte)
        return index

    def modifica(self, id_carte, titlu_nou, descriere_noua, autor_nou):
        """
        Metoda care modifica datele unei carti cu id-ul dat
        :param id_carte:
        :param titlu_nou:
        :param descriere_noua:
        :param autor_nou:
        """
        self.__repository.modifica(id_carte, titlu_nou, descriere_noua, autor_nou)
