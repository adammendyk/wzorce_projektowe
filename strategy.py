from abc import ABCMeta, abstractmethod


class ISpetialization(metaclass=ABCMeta):

    @abstractmethod
    def do(self):
        pass


class Painter(ISpetialization):

    def do(self):
        print('paint...')


class Librarian(ISpetialization):

    def do(self):
        print('doint something in library')


class Person:

    def __init__(self, name, spetialization):
        self.name = name
        self.spetialization = spetialization

    def do(self):
        if self.spetialization is not None:
            self.spetialization.do()
        else:
            print("I'm a student, just learning")

    def set_spetialization(self, spetialization):
        self.spetialization = spetialization


def main():
    bob = Person('Bob', None)
    sam = Person('Sam', None)

    bob.do()
    sam.do()

    bob.set_spetialization(Librarian())
    bob.do()

    sam.set_spetialization(Painter())
    sam.do()


if __name__ == '__main__':
    main()
