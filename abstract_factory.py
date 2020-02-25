from abc import ABCMeta, abstractmethod


class Beer(metaclass=ABCMeta):
    pass


class Tuborg(Beer):
    pass


class Staropramen(Beer):
    pass


class Komes(Beer):
    pass


class Snack(metaclass=ABCMeta):

    @abstractmethod
    def interact(self, beer: Beer) -> None:
        pass


class Peanuts(Snack):

    def interact(self, beer: Beer) -> None:
        print(f'Drinking some {beer.__class__.__name__} with peanuts')


class Chips(Snack):

    def interact(self, beer: Beer) -> None:
        print(f'Drinking some {beer.__class__.__name__} with chips')


class Crostini(Snack):

    def interact(self, beer: Beer) -> None:
        print(f'Drinking some {beer.__class__.__name__} with crostini')


class AbstractShop(metaclass=ABCMeta):

    @abstractmethod
    def buy_beer(self) -> Beer:
        pass

    @abstractmethod
    def buy_snack(self) -> Snack:
        pass


class ExpensiveShop(AbstractShop):

    def buy_beer(self) -> Beer:
        return Tuborg()

    def buy_snack(self) -> Snack:
        return Peanuts()


class CheapShop(AbstractShop):

    def buy_beer(self) -> Beer:
        return Staropramen()

    def buy_snack(self) -> Snack:
        return Chips()


class LocalShop(AbstractShop):

    def buy_beer(self) -> Beer:
        return Komes()

    def buy_snack(self) -> Snack:
        return Crostini()


def main():
    expensive_shop = ExpensiveShop()
    beer = expensive_shop.buy_beer()
    snack = expensive_shop.buy_snack()
    snack.interact(beer)

    cheap_shop = CheapShop()
    snack = cheap_shop.buy_snack()
    beer = cheap_shop.buy_beer()
    snack.interact(beer)

    local_shop = LocalShop()
    snack = local_shop.buy_snack()
    beer = local_shop.buy_beer()
    snack.interact(beer)


if __name__ == '__main__':
    main()
