
from Controller.Coffee_controller import CoffeeController
from Repository.Coffee_repository import CoffeeRepository
from Teste.tests import testing
from UI.Console import Console


coffee_repository = CoffeeRepository('Files/coffees.txt')
coffee_controller = CoffeeController(coffee_repository)
coffee_repository_test = CoffeeRepository('Files/coffees_test.txt')
coffee_controller_test = CoffeeController(coffee_repository_test)
testing(coffee_repository_test, coffee_controller_test)


ui = Console(coffee_controller)


ui.program()
