#!/usr/bin/python
from logging import info


class FileFormatException(IOError):
    pass


def file_reader(path):
    """
    dorobic yeild wyrzucajace krotki, lub listy z danymi po splicie,
    gotowe do porownan
    """
    pass


file_name = './wzorce_projektowe/accessories.txt'

with open(file_name) as f:
    data_file = f.readlines()

    def get_max_accessories(f):
        max_products = [0, 0]
        current_max = []
        for line in data_file:
            splitted = line.strip().split(':')
            current_max = [int(splitted[0]), len(splitted[1].split(','))]
            if max_products[1] < current_max[1]:
                max_products = current_max
        return tuple(max_products)
        # try:
        #     products = {}
        #     for line in data_file:
        #         line_splited = line.split(":")
        #         if len(line_splited) != 2:
        #             raise FileFormatException("Line cannot be split by ':'")
        #         product_id, accessories = line_splited
        #         accessories = accessories.split(",")
        #         products[product_id] = len(accessories)
        #     return sorted(products.items(), key=lambda x: x[1], reverse=True)[0]
        # except FileFormatException:
        #     info("Bad input file. Please check format of your file")
        #     raise
        # except IOError:
        #     info("Some I/O Problems")
        # return []


def main():
    print(get_max_accessories(file_name))


if __name__ == '__main__':
    main()
