from abc import ABCMeta, abstractmethod


class Car:

    def __init__(self, wheels=4, seats=4, color="Black"):
        self.wheels = wheels
        self.seats = seats
        self.color = color

    def __str__(self):
        return f"This is a {self.color} car with " \
            f"{self.wheels} wheels and {self.seats} seats."


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_seats(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CarBuilder(Builder):

    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value
        return self

    def set_seats(self, value):
        self.car.seats = value
        return self

    def set_color(self, value):
        self.car.color = value
        return self

    def get_result(self):
        return self.car


class CarBuilderDirector:

    @staticmethod
    def construct():
        builder = CarBuilder()
        model = builder.set_wheels(8).set_seats(4).set_color("Red")
        return model.get_result()


def main():
    car = CarBuilderDirector.construct()
    print(car)


if __name__ == '__main__':
    main()
