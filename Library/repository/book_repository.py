from domain.Colors import X
from repository.txtrepository import TxtRepository
from ui.listaprecompletata import lista_precompletata_inchiriate, lista_precompletata_carti


class BookRepository:

    def __init__(self, repository_txt):
        self.txt_repository = repository_txt
        self.__list_books = self.txt_repository.returnare()
        self.__lista_inchiriate = lista_precompletata_inchiriate()

    def get_all(self):
        return self.__list_books

    def get_all_inchiriate(self):
        return self.__lista_inchiriate

    def adauga(self, book):
        """
        Metoda care adauga o noua carte in lista
        :param book:
        :return:
        Arunca o eroare daca id-ul cartii pe care vrem sa o introducem exista deja in lista. Eroarea e tratata
            in UI.
        """
        if self.gaseste_carte_dupa_id(book.id) != -1:
            raise KeyError(X('\033[91m There is already a book with this id! \033[0m'))
        else:
            self.__list_books.append(book)

    def add_fisier(self, id, titlu, descriere, autor):
        self.txt_repository.store_to_file(id, titlu, descriere, autor)

    def sterge(self, id_carte):
        """
        Metoda care sterge o carte din lista
        :param id_carte:
        :return:
        Arunca o eroare daca id-ul cartii pe care vrem sa o stergem nu exista in lista. Eroarea e tratata in
            UI.
        """
        if self.gaseste_carte_dupa_id(id_carte) == -1:
            raise KeyError(X('\033[91m The book with this id does not exist! \033[0m'))
        else:
            index = self.gaseste_carte_dupa_id(id_carte)
            self.__list_books.pop(index)

    def modifica(self, id_carte, titlu_nou, descriere_noua, autor_nou):
        """
        Metoda care modifica o carte din lista
        :param id_carte:
        :param titlu_nou:
        :param descriere_noua:
        :param autor_nou
        :return:
        Arunca o eroare daca id-ul cartii pe care vrem sa o modificam nu exista in lista. Eroarea e
            tratata in UI.
        """
        if self.gaseste_carte_dupa_id(id_carte) == -1:
            raise KeyError(X('\033[91m The book with this id does not exist!\033[0m'))
        else:
            index = self.gaseste_carte_dupa_id(id_carte)
            carte = self.__list_books[index]
            carte.titlu = titlu_nou
            carte.descriere = descriere_noua
            carte.autor = autor_nou

    def gaseste_carte_dupa_id(self, id_carte):
        """
        Metoda care returneaza pozitia in lista de carti a unei carti, dupa id
        :param id_carte:
        :return: pozitia cartii in lista, daca ea exista in lista de carti; -1, altfel
        """
        for i in range(0, len(self.__list_books)):
            carte_curenta = self.__list_books[i]
            if carte_curenta.id == id_carte:
                return i
        return -1

    def gaseste_carte_inchiriata(self, id_carte):
        for i in range(0, len(self.__lista_inchiriate)):
            carte_curenta = self.__lista_inchiriate[i]
            if carte_curenta.id == id_carte:
                return i
        return -1

    def lista_carti_inchiriate(self, id_carte):
        index = self.gaseste_carte_dupa_id(id_carte)
        carte = self.__list_books[index]
        self.__lista_inchiriate.append(carte)
        self.sterge(id_carte)

    def returnare_carte(self, id_carte):
        index = self.gaseste_carte_inchiriata(id_carte)
        carte = self.__lista_inchiriate[index]
        self.__list_books.append(carte)
        self.__list_books.sort(key=lambda x: x.id)

    def afisare_carti(self, id_carte):
        index = self.gaseste_carte_inchiriata(id_carte)
        carte = self.__lista_inchiriate[index]
        return carte
