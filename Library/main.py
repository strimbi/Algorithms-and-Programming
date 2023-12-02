from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.InchiriereController import InchiriereController
from repository.book_repository import BookRepository, TxtRepository
from repository.client_repository import ClientRepository
from repository.inchiriere_repository import InchiriereRepository
from test.teste import TesteCod
from ui.console import Console

TesteCod()

repository_txt = TxtRepository('repository/liste')
book_repository = BookRepository(repository_txt)
client_repository = ClientRepository()
inchiriere_repository = InchiriereRepository(book_repository, client_repository)


book_controller = BookController(book_repository)
client_controller = ClientController(client_repository)
inchiriere_controller = InchiriereController(inchiriere_repository, book_repository, client_repository)

ui = Console(book_controller, client_controller, inchiriere_controller)

ui.program()
