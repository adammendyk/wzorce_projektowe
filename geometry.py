import math


class BadDataException(Exception):
    def __init_subclass__(cls):
        msg = 'Wrong data format'
        super().__init_subclass__(msg)


def cross_product(v1, v2):
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v2[2] * v1[0],
        v1[0] * v2[1] - v1[1] * v2[0]
    )


def substract(v1, v2):
    return(
        v1[0] - v2[0],
        v1[1] - v2[1],
        v1[2] - v2[2]
    )


def distance(p1, p2):
    delta = substract(p1, p2)
    return math.sqrt(dot_product(delta, delta))


def dot_product(v1, v2):
    return sum([v1[0] * v2[0], v1[1] * v2[1], v1[2] * v2[2]])


# line = (start_point, direction)
# start_point = (x, y, z)
# direction = (nx, ny, nz)


def line_distance(l1, l2):
    # l = (a, b, c, nx, ny, nz) <- definicja linii - 6 parametrów
    """
    DOCSTRING here; refer to https://en.wikipedia.org/wiki/Skew_lines#Distance
    """

    n = cross_product(l1, l2)
    n1 = cross_product(n, l1)
    n2 = cross_product(n, l2)

    # cross point 1, multiplier = dotproduct  v1, n2
    multiplier_n = 1
    multiplier_n = dot_product(n2, v1) / multiplier_n

    if not multiplier_n:
        raise BadDataException

    wagedpoint1 = substract(l2, l1)

    multiplier1 = 1
    multiplier1 = dot_product(n2, wagedpoint1) / multiplier1

    # c1 = p1[0,1,2] + multiplier * v2[0,1,2]
    c1 = [0, 0, 0]
    c1[0] = p1[0] + multiplier1 * p2[0]
    c1[1] = p1[1] + multiplier1 * p2[1]
    c1[2] = p1[2] + multiplier1 * p2[2]

    # multiplier = v2[0] * n1[0] + v2[1] * n1[1] + v2[2] * n1[2]
    multiplier2 = dot_product(l2, n1)

    if not multiplier2:
        raise BadDataException

    wagedpoint2 = substract(l1, l2)

    multiplier2 = 1
    multiplier2 = dot_product(n1, wagedpoint1) / multiplier2

    # c2 = p2[0,1,2] + multiplier * v1[3,4,5]
    c2 = [0, 0, 0]
    c2[0] = p2[0] + multiplier2 * v1[0]
    c2[1] = p2[1] + multiplier2 * v1[1]
    c2[2] = p2[2] + multiplier2 * v1[2]

    return distance(c1, c2)


l1 = [2, 3, 2, 1, 2, 1]
l2 = [3, 4, 5, 1, 1, 2]
p1, p2 = l1[:3], l2[:3]
v1, v2 = l1[3:], l2[3:]


def main():
    print(line_distance(l1, l2))


if __name__ == "__main__":
    main()
