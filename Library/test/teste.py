from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.InchiriereController import InchiriereController
from domain.Book import Book
from domain.Client import Client
from domain.Inchiriate import Inchiriate
from domain.Numarinchirieri import Numarinchirieri
from repository.book_repository import BookRepository
from repository.client_repository import ClientRepository
import unittest
from repository.inchiriere_repository import InchiriereRepository
from ui.listaprecompletata import lista_precompletata_carti


class TesteCod(unittest.TestCase):

    def test_carte(self):
        carte1 = Book(1, 'Matematica', 'Superba', 'Mariana')
        self.assertEqual(carte1.get_id(), 1)
        self.assertEqual(carte1.get_titlu(), "Matematica")
        self.assertEqual(carte1.get_descriere(), "Superba")
        self.assertEqual(carte1.get_autor(), "Mariana")
        self.assertEqual(carte1.__str__(), "Carte 1 || Titlu: Matematica / Descriere: Superba / Autor: Mariana")
        carte1.set_id(2)
        carte1.set_titlu("Mate-info")
        carte1.set_descriere("Extra")
        carte1.set_autor("Marienette")
        self.assertEqual(carte1.get_id(), 2)
        self.assertEqual(carte1.get_titlu(), "Mate-info")

    def test_client(self):
        client1 = Client(1, 'Victor', '818724')
        self.assertEqual(client1.id, 1)
        self.assertEqual(client1.nume, 'Victor')
        self.assertEqual(client1.cnp, '818724')
        self.assertEqual(client1.__str__(), "Client 1 || Nume: Victor / Cnp: 818724")
        client1.id = 2
        client1.nume = "Veronica"
        client1.cnp = "6847123"
        self.assertEqual(client1.id, 2)
        self.assertEqual(client1.nume, "Veronica")
        self.assertEqual(client1.cnp, "6847123")

    def teste_diverse(self):
        lista = lista_precompletata_carti()
        self.assertEqual(4, len(lista))

    def teste_inchiriate(self):
        inchiriat = Inchiriate(1, 3)
        self.assertEqual(1, inchiriat.id_client)
        self.assertEqual(3, inchiriat.id_carte)
        inchiriat.id_carte = 2
        inchiriat.id_client = 2
        self.assertEqual(2, inchiriat.id_carte)
        self.assertEqual(2, inchiriat.id_client)
        self.assertEqual(inchiriat.__str__(), "Client: 2 || Carte: 2")

    def teste_numar_inchirieri(self):
        numar = Numarinchirieri(1, 2, 'Maria')
        self.assertEqual(1, numar.id_client)
        self.assertEqual('Maria', numar.nume)
        self.assertEqual(2, numar.numar_carti)
        numar.id_client = 2
        numar.nume = 'Paula'
        numar.numar_carti = 3
        self.assertEqual(2, numar.id_client)
        self.assertEqual('Paula', numar.nume)
        self.assertEqual(3, numar.numar_carti)
        self.assertEqual(numar.__str__(), "Client: 2 || Nume: Paula || Numar carti: 3")

    def test_client_repository(self):
        repository = ClientRepository()
        lista_clienti = repository.get_all()
        repository.modifica(1, "Carla", "418921")
        self.assertEqual(len(lista_clienti), 2)
        self.assertEqual(repository.gaseste_client_dupa_id(1), 0)
        self.assertEqual(repository.gaseste_client_dupa_id(4), -1)
        repository.sterge(1)
        self.assertEqual(len(lista_clienti), 1)
        self.assertEqual(repository.gaseste_client_dupa_id(1), -1)

    def test_book_repository(self):
        repository = BookRepository()
        lista_carti = repository.get_all()
        self.assertEqual(4, len(lista_carti))
        carte = Book(5, 'Lol', 'Meh', 'Marius')
        repository.adauga(carte)
        self.assertIn(carte, repository.get_all())

    def test_book_controller(self):
        repository = BookRepository()
        controller = BookController(repository)
        self.assertEqual(len(controller.get_all()), 4)
        controller.adauga(5, 'Ursul Fram', 'Trista', 'Jack')
        self.assertEqual(len(controller.get_all()), 5)
        controller.sterge(5)
        self.assertEqual(len(controller.get_all()), 4)
        controller.modifica(3, 'Peter Pan', 'Fericita', 'Jamila')
        self.assertEqual(len(controller.get_all()), 4)
        lista_inchiriate = controller.get_all_inchiriate()
        self.assertListEqual(lista_inchiriate, [])
        self.assertEqual(controller.cauta(2), 1)

    def test_clienti_controller(self):
        repository = ClientRepository()
        controller = ClientController(repository)
        lista_clienti = controller.get_all()
        self.assertEqual(len(lista_clienti), 2)
        controller.adauga(3, "Bogdan", "8414334")
        self.assertEqual(len(lista_clienti), 3)
        controller.modifica(1, "Andreea", "894132")
        self.assertEqual(len(lista_clienti), 3)
        controller.sterge(1)
        self.assertEqual(len(lista_clienti), 2)
        self.assertEqual(controller.cauta(2), 0)

    def test_inchiriere_controller(self):
        book_repository = BookRepository()
        client_repository = ClientRepository()
        repository = InchiriereRepository(book_repository, client_repository)
        controller = InchiriereController(repository, book_repository, client_repository)
        controller.inchiriere_carte(1, 3)
        self.assertEqual(len(book_repository.get_all()), 3)
        self.assertEqual(len(repository.get_all_numar()), 1)
        self.assertEqual(len(repository.get_all_inchirieri()), 1)
        self.assertEqual(book_repository.gaseste_carte_inchiriata(3), 0)
        controller.returnare_carte(1, 3)
        self.assertEqual(len(book_repository.get_all()), 4)
        self.assertEqual(len(repository.get_all_numar()), 1)
        self.assertEqual(len(repository.get_all_inchirieri()), 1)

    def test_inchiriate_controller_2(self):
        book_repository = BookRepository()
        client_repository = ClientRepository()
        repository = InchiriereRepository(book_repository, client_repository)
        controller = InchiriereController(repository, book_repository, client_repository)
        controller.inchiriere_carte(1, 3)
        controller.inchiriere_carte(2, 4)
        lista = controller.afisare_clienti_dupa_nume()
        self.assertEqual(2, len(lista))
        controller.inchiriere_carte(2, 1)
        lista = controller.cei_mai_activi_clienti()
        self.assertEqual(1, len(lista))
        lista = controller.top_carti_inchiriate()
        self.assertEqual(2, len(lista))
        self.assertEqual(book_repository.gaseste_carte_inchiriata(4), 1)
        self.assertEqual(book_repository.gaseste_carte_inchiriata(7), -1)

    def test_inchiriere_repository(self):
        book_repository = BookRepository()
        client_repository = ClientRepository()
        repository = InchiriereRepository(book_repository, client_repository)
        obiect = Inchiriate(1, 3)
        repository.inchiriere(obiect, 1, 3)
        self.assertEqual(repository.gaseste_pozitie_client(1), 0)
        self.assertEqual(repository.gaseste_pozitie_client(2), -1)


if __name__ == '__main__':
    unittest.main()
