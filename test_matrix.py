from unittest import TestCase
from transform import Matrix

__author__ = 'Judd'


class TestMatrix(TestCase):
    def test_rotate_1(self):
        start = [
            [1, 2, 1],
            [2, 2, 2],
            [2, 1, 2],
        ]

        m = Matrix(start)
        rotated = m.rotate_n(1)

        end = [
            [1, 2, 2],
            [2, 2, 1],
            [1, 2, 2],
        ]

        self.assertEqual(rotated, end)

    def test_rotate_2(self):
        start = [
            [1, 2, 1],
            [2, 2, 2],
            [2, 1, 2],
        ]

        m = Matrix(start)
        rotated = m.rotate_n(2)

        end = [
            [2, 1, 2],
            [2, 2, 2],
            [1, 2, 1],
        ]

        self.assertEqual(rotated, end)

    def test_rotate_3(self):
        start = [
            [1, 2, 1],
            [2, 2, 2],
            [2, 1, 2],
        ]

        m = Matrix(start)
        rotated = m.rotate_n(3)

        end = [
            [2, 2, 1],
            [1, 2, 2],
            [2, 2, 1],
        ]

        self.assertEqual(rotated, end)

    def test_rotate_4(self):
        start = [
            [1, 2, 1],
            [2, 2, 2],
            [2, 1, 2],
        ]

        m = Matrix(start)
        rotated = m.rotate_n(4)

        end = [
            [1, 2, 1],
            [2, 2, 2],
            [2, 1, 2],
        ]

        self.assertEqual(rotated, end)