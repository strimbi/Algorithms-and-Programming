from domain.Book import Book
from domain.Client import Client


def lista_precompletata_carti():

    lista_carti = [Book(1, 'Micul Print', 'Super', 'Antoine'), Book(2, 'Istoria Lumii', 'Naspa', 'Daria'),
                   Book(3, 'Otilia', 'Mediu', 'Calinescu'), Book(4, 'Plumb', 'Trista', 'Bacovia')]
    return lista_carti


def lista_precompletata_clienti():
    lista_clienti = [Client(1, 'Maria', '07224561'), Client(2, 'Alex', '94284327')]
    return lista_clienti


def lista_precompletata_inchirieri():
    lista_inchirieri = []
    return lista_inchirieri


def lista_precompletata_numar_inchirieri():
    numar_inchirieri = []
    return numar_inchirieri


def lista_precompletata_clienti_inchiriere():
    lista_clienti_inchiriere = []
    return lista_clienti_inchiriere


def lista_precompletata_inchiriate():
    lista_inchiriate = []
    return lista_inchiriate
