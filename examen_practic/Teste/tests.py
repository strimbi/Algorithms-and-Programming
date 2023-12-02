from Domain.Coffe import Coffee


class Tests:

    def __init__(self, coffee_repository, coffee_controller):
        self.repository = coffee_repository
        self.controller = coffee_controller

    def test_domain(self):
        coffee = Coffee(383, "Black", "England", 14.0)
        assert (coffee.name == "Black")
        assert (coffee.id == 383)
        assert (coffee.country == "England")
        assert (coffee.price == 14.0)

    def test_repository(self):
        assert (self.repository.return_all() == [Coffee(id=321, name='Black', country='England', price=14.0),
                                                 Coffee(id=645, name='Green', country='France', price=30.0),
                                                 Coffee(id=312, name='Honey', country='Spain', price=15.5),
                                                 Coffee(id=315, name='Ginger', country='Germany', price=40.0),
                                                 Coffee(id=431, name='Berries', country='Romania', price=13.6)])

    def test_controller(self):
        assert (self.controller.return_all() == [Coffee(id=321, name='Black', country='England', price=14.0),
                                                 Coffee(id=645, name='Green', country='France', price=30.0),
                                                 Coffee(id=312, name='Honey', country='Spain', price=15.5),
                                                 Coffee(id=315, name='Ginger', country='Germany', price=40.0),
                                                 Coffee(id=431, name='Berries', country='Romania', price=13.6)])

        assert (self.controller.return_by_country(country="Germany")) == [Coffee(id=315, name='Ginger',
                                                                                 country='Germany', price=40.0)]

    def run_tests(self):
        self.test_controller()
        self.test_repository()
        self.test_domain()
        print("All tests have passed!")


def testing(coffee_repository, coffee_controller):
    repo = Tests(coffee_repository, coffee_controller)
    repo.run_tests()
