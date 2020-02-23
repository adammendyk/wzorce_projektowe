import geometry
import unittest


# l1 = [2, 3, 2, 1, 2, 1]
# l2 = [3, 4, 5, 1, 1, 2]
# p1, p2 = l1[:4], l2[:4]
# v1, v2 = l1[3:], l2[3:]


class GeomertyTestCase(unittest.TestCase):

    def test_substract(self):
        self.assertEqual(geometry.substract([1, 2, 1], [1, 1, 2]), (0, 1, -1))

    def test_cross_product(self):
        self.assertEqual(geometry.cross_product(
            [1, 2, 1], [1, 1, 2]), (3, -1, -1))

    def test_distance(self):
        self.assertEqual(geometry.distance(
            [2, 3, 2], [3, 4, 5]), 3.3166247903554)

    def test_dot_product(self):
        self.assertEqual(geometry.dot_product(
            [1, 2, 1], [1, 1, 2]), 5)

    def test_line_distance(self):
        self.assertEqual(geometry.line_distance(
            [2, 3, 2, 1, 2, 1], [3, 4, 5, 1, 1, 2]), 320.0671804481053)
