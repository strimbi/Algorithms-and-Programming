

class CoffeeController:

    def __init__(self, coffee_repository):
        self.repository = coffee_repository

    def return_all(self):
        """
        Returneaza lista cu cafele
        :return:
        """
        return self.repository.return_all()

    def add_coffee(self, id_c, name, country, price):
        """
        Trimite in repository datele pt a adauga o cafea noua
        :param id_c:
        :param name:
        :param country:
        :param price:
        :return:
        """
        self.repository.add_coffee(id_c, name, country, price)

    def return_by_country(self, country):
        """
        Returneaza lista cu cafele provenite dintr o tara anume
        :param country:
        :return:
        """
        return self.repository.return_coffee_by_country(country)
