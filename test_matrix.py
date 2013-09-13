from unittest import TestCase
from transform import Matrix
import transform

__author__ = 'Judd'

class TestMatchAllTransformations(TestCase):
    def test_carrier_positions(self):
        board = [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 2, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 2, 0, 1, 1, 1],
            [1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1],
            [1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        shape = [
            [0,0,0],
            [5,0,5],
            [5,0,5],
            [5,0,5]
        ]

        co_ords = [
            (0,0),
            (0,1),
            (0,2),
            (1,1),
            (2,1),
            (2,1)
        ]

        bla = transform.ShapeAndCoOrds(shape, co_ords)

        single_matches = []

        for result in bla.all_transformations():
            matches = transform.match_matrix(result[0], board)

            for j, i in matches: # reversed on purpose
                single_matches.append((i, j))

        self.assertCountEqual(single_matches, [
            (6,6),
            (6,7),
            (7,6),
            (7,6),
            (1,1)
        ])

    def test_carrier_squares(self):
        board = [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 2, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 2, 0, 1, 1, 1],
            [1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 2, 1],
            [1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 2, 2, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        shape = [
            [0,0,0],
            [5,0,5],
            [5,0,5],
            [5,0,5]
        ]

        co_ords = [
            (0,0),
            (0,1),
            (0,2),
            (1,1),
            (2,1),
            (3,1)
        ]

        bla = transform.ShapeAndCoOrds(shape, co_ords)

        allowed_points =  []
        single_matches = []

        for result in bla.all_transformations():
            matches = transform.match_matrix(result[0], board)

            for j, i in matches: # reversed on purpose
                single_matches.append((i, j))

                for relative_tuple in result[1]:
                    allowed_points.append((i+relative_tuple[0], j+relative_tuple[1]))

        self.assertCountEqual(single_matches, [
            (7,6),
            (7,6)
        ])

        self.assertCountEqual(tuple(allowed_points), [
            # horizonal at 7,6
            (7,6),
            (8,6),
            (9,6),
            (8,7),
            (8,8),
            (8,9),

            # horizonal at 7,6 other way
            (8,6),
            (8,7),
            (8,8),
            (8,9),
            (7,9),
            (9,9),
        ])

    def test_hovercraft_positions(self):
        board = [
            [2, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 2, 2, 2],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 2, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
        ]

        shape = [
            [5,0,5],
            [0,0,0],
            [0,5,0]
        ]

        co_ords = [
            (0,1),
            (1,0),
            (2,0),
            (1,1),
            (1,2),
            (2,2)
        ]

        bla = transform.ShapeAndCoOrds(shape, co_ords)

        allowed_points =  []
        single_matches = []

        for result in bla.all_transformations():
            matches = transform.match_matrix(result[0], board)

            for j, i in matches: # reversed on purpose
                single_matches.append((i, j))

                for relative_tuple in result[1]:
                    allowed_points.append((i+relative_tuple[0], j+relative_tuple[1]))

        self.assertCountEqual(single_matches, [
            (6,0),
            (9,9)
        ])

        self.assertCountEqual(allowed_points, [
            (7,0),
            (8,0),
            (6,1),
            (7,1),
            (7,2),
            (8,2)
        ])

class TestPatternMatching(TestCase):
    def test_elimination(self):
        config = [[1, 1, 0, 1, 1, 0],
                  [0, 2, 2, 2, 2, 0],
                  [0, 1, 0, 0, 1, 0],
                  [1, 1, 0, 1, 0, 0],
                  [1, 2, 0, 0, 1, 0],
                  [0, 2, 0, 0, 0, 1],
                  [1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                  [0, 1, 0, 0, 1, 0, 0, 1, 1, 2, 2, 1],
                  [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 1, 0],
                  [0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 0],
                  [0, 1, 1, 1, 2, 2, 0, 1, 2, 2, 2, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]]

        matches = transform.match_matrix([[0,0,0],
                                          [5,0,5],
                                          [5,0,5],
                                          [5,0,5]], config)

        co_ords = []

        for j, i in matches:
            co_ords.append((i, j))

        self.assertSequenceEqual(co_ords, [
            (6, 5)
        ])

    def test_slice_overlap(self):
        slices = transform.slice_overlap([1,2,3,4,5], 2)
        response = [
            [1,2],
            [2,3],
            [3,4],
            [4,5]
        ]
        self.assertSequenceEqual(tuple(slices), tuple(response))

    def test_match_row(self):
        matches = transform.match_row([2,1], [2,1,2,1])

        self.assertSequenceEqual(tuple(matches), tuple([0,2]))

    def test_match_row_2(self):
        matches = transform.match_row([2], [1,2,1,2,1])

        self.assertSequenceEqual(tuple(matches), tuple([1,3]))

    def test_group_matches(self):
        row_matches = [
            [0,1,2,3],
            [0,1],
            [1,3]
        ]
        grouped = transform.group_matches(row_matches)
        expected = [1]
        self.assertSequenceEqual(tuple(grouped), tuple(expected))

    def test_group_matches_2(self):
        row_matches = [
            [0,1,2,3,4],
            [2],
            [1,2,3],
            [0,2,4]
        ]
        grouped = transform.group_matches(row_matches)
        expected = [2]
        self.assertListEqual(grouped, expected)

    def test_same_height(self):
        test_pattern = [
            [1],
            [2],
            [2],
            [1]
        ]

        ship = [
            [1, 1, 2, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 1, 1]
        ]

        result = transform.group_matches(transform.match_matrix_same_height(test_pattern, ship))
        self.assertListEqual(result, [1,3])

    def test_same_height_2(self):
        test_pattern = [
            [1],
            [2],
            [2],
            [1]
        ]

        ship = [
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1]
        ]

        expected = [
            [0,1,2,3,4],
            [2],
            [1,2,3],
            [0,2,4]
        ]

        result = transform.match_matrix_same_height(test_pattern, ship)

        # test generator of generators
        for index, row in enumerate(result):
            self.assertSequenceEqual(tuple(row), tuple(expected[index]))

    def test_same_height_grouped(self):
        test_pattern = [
            [1],
            [2],
            [2],
            [1]
        ]

        ship = [
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1]
        ]

        ungrouped = transform.match_matrix_same_height(test_pattern, ship)
        grouped = transform.group_matches(ungrouped)

        self.assertListEqual(grouped, [2])

    def test_matrix(self):
        test_pattern = [
            [1],
            [2],
            [2],
            [1]
        ]

        ship = [
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 1, 1]
        ]

        expected = [
            (2,0),
            (1,1),
            (3,1)
        ]

        row_results = transform.match_matrix(test_pattern, ship)

        for index, row in enumerate(row_results):
            self.assertSequenceEqual(tuple(row), tuple(expected[index]))

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