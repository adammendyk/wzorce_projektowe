from abc import ABCMeta, abstractmethod


class Car:

    def __init__(self, wheels=4, seats=4, color="Black", doors=4):
        self.wheels = wheels
        self.seats = seats
        self.color = color
        self.doors = doors

    def __str__(self):
        return f"This is a {self.color} car with " \
            f"{self.wheels} wheels, {self.doors} doors and {self.seats} seats."


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

    @abstractmethod
    def set_doors(self):
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

    def set_doors(self, value):
        self.car.doors = value
        return self

    def get_result(self):
        return self.car


class CarBuilderDirector:

    @staticmethod
    def construct():
        builder = CarBuilder()
        model = builder.set_wheels(8).set_seats(
            4).set_color("Red").set_doors(2)
        return model.get_result()


def main():
    car = CarBuilderDirector.construct()
    print(car)


if __name__ == '__main__':
    main()
