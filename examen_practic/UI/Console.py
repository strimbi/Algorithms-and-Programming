
class Console:

    def __init__(self, coffee_controller):
        self.controller = coffee_controller

    @staticmethod
    def menu():
        """
        Creez meniul pt a afisa functionalitatile programului
        :return:
        """
        menu = ""
        menu += "1. Print coffees\n"
        menu += "2. Add coffee\n"
        menu += "3. Print coffees from a certain country\n"
        menu += "0. Exit\n"
        return menu

    def program(self):
        run = True
        while run:
            menu = self.menu()
            print(menu)
            command = input("Input command: ")
            if command == "1":
                self.ui_print()
            elif command == "2":
                self.ui_add_coffee()
            elif command == "3":
                self.ui_return_cof_by_country()
            elif command == "0":
                run = False
            else:
                "Wrong command! Try again"

    def ui_print(self):
        list_coffee = self.controller.return_all()
        if list_coffee == -1:
            print("List is empty!")
        else:
            for coffee in list_coffee:
                print(coffee)

    def ui_add_coffee(self):
        ok = 1
        id_c = int(input("Set id: "))
        name = input("Set name: ")
        if len(name) < 3:
            print("The name should be longer than 3 letters!")
            ok = 0
        country = input("Set country of origin: ")
        price = float(input("Set price: "))
        if price <= 0:
            print("The price should be higher than 0!")
            ok = 0
        if ok!= 0:
            self.controller.add_coffee(id_c, name, country, price)

    def ui_return_cof_by_country(self):
        country = input("What country of origin? ")
        list_cof = self.controller.return_by_country(country)
        for coffee in list_cof:
            print(coffee)
