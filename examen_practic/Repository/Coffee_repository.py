from Domain.Coffe import Coffee


class CoffeeRepository:

    def __init__(self, coffee_txt):
        self.coffee_txt = coffee_txt
        self.list_coffees = []
        self.read_file()

    def read_file(self):
        """
        Citesc din fisier cafelele si creez o lista cu ele
        :return:
        """
        with open(self.coffee_txt, 'r') as f:
            for line in f:
                line = line.split(',')
                id_c = int(line[0])
                name = str(line[1])
                country = str(line[2])
                price = float(line[3])
                self.list_coffees.append(Coffee(id_c, name, country, price))

    def write_file(self):
        """
        Rescriu fisierul cu lista de cafele
        :return:
        """
        with open(self.coffee_txt, 'w') as f:
            for coffee in self.list_coffees:
                strid = str(coffee.id) + ',' + str(coffee.name) + ',' + str(coffee.country) + ',' + str(coffee.price) +\
                        '\n'
                f.write(strid)

    def return_all(self):
        """
        Returnez lista cu cafele, iar daca e goala afisez o eroare
        :return:
        """
        if len(self.list_coffees) != 0:
            return self.list_coffees
        else:
            return -1

    def add_coffee(self, id_c, name, country, price):
        """
        Adaug o cafea noua in lista daca nu mai exista cafele cu acelasi nume si id
        :param id_c:
        :param name:
        :param country:
        :param price:
        :return:
        """
        coffee = Coffee(id_c, name, country, price)
        if self.find_coffee(id_c) == -1:
            print("This id is used! Try again")
        elif self.find_coffee_name(name) == -1:
            print("This name is used! Try again")
        else:
            self.list_coffees.append(coffee)
            self.write_file()

    def return_coffee_by_country(self, country):
        """
        Returnez o lista cu cafelele dintr o tara anume
        :param country
        :return:
        """
        list_of_coffee = []
        for coffee in self.list_coffees:
            if coffee.country == country:
                list_of_coffee.append(coffee)
        return list_of_coffee

    def find_coffee(self, id_c):
        """
         Gasesc daca mai exista o cafea cu acest id in lista
         :param id_c
         :return:
         """
        for coffee in self.list_coffees:
            if coffee.id == id_c:
                return -1

    def find_coffee_name(self, name):
        """
        Gasesc daca mai exista o cafea cu acest nume in lista
        :param name:
        :return:
        """
        for coffee in self.list_coffees:
            if coffee.name == name:
                return -1
