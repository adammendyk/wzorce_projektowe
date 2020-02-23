from abc import ABCMeta, abstractmethod


class AbstractShippingProvider(metaclass=ABCMeta):

    @abstractmethod
    def calculate_cost(self):
        raise NotImplementedError


class FedEx(AbstractShippingProvider):

    def __init__(self, rate):
        self._rate = rate

    def calculate_cost(self):
        return self._rate


class PostPoland(AbstractShippingProvider):

    def calculate_cost(self):
        return 42


class Calculator:

    def __init__(self, shipping_provider):
        self.shipping_provider = shipping_provider

    def calculate(self, mass, height, width):
        if self.shipping_provider is None:
            raise Exception('No shipping provider set')
        else:
            return self.shipping_provider.calculate_cost()

    def set_shipping_provider(self, new_shipping_provider):
        self.shipping_provider = new_shipping_provider


def main():
    post_poland = PostPoland()
    shipping_calculator = Calculator(post_poland)

    cost = shipping_calculator.calculate(15, 10, 20)
    print(f'Shipping cost with Post Poland is {cost}')

    fedex = FedEx(rate=100)
    shipping_calculator.set_shipping_provider(fedex)

    cost = shipping_calculator.calculate(15, 10, 20)
    print(f'Shipping cost with FedEx is {cost}')


if __name__ == '__main__':
    main()

