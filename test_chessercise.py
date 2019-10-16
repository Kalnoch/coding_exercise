__author__ = 'Stuart Glassett'

import unittest
from chessercise import Chessercise


class TestPosition(unittest.TestCase):
    def setUp(self):
        self.chess = Chessercise()

    def test_good_position(self):
        self.assertEqual(self.chess.text_to_position("d3"), (3, 2))

    def test_bad_position(self):
        self.assertIsNone(self.chess.text_to_position("q9"))


class TestKnight(unittest.TestCase):
    def setUp(self):
        self.chess = Chessercise()

    def test_corner(self):
        correct = ['b3', 'c2']
        answer = self.chess.calc_knight((0, 0))
        answer.sort()
        self.assertEqual(answer, correct)

    def test_middle(self):
        correct = ['b2', 'b4', 'c1', 'c5', 'e1', 'e5', 'f2', 'f4']
        answer = self.chess.calc_knight((3, 2))
        answer.sort()
        self.assertEqual(answer, correct)


class TestRook(unittest.TestCase):
    def setUp(self):
        self.chess = Chessercise()

    def test_corner(self):
        correct = ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
        answer = self.chess.calc_rook((0, 0))
        answer.sort()
        self.assertEqual(answer, correct)

    def test_middle(self):
        correct = ['a3', 'b3', 'c3', 'd1', 'd2', 'd4', 'd5', 'd6', 'd7', 'd8', 'e3', 'f3', 'g3', 'h3']
        answer = self.chess.calc_rook((3, 2))
        answer.sort()
        self.assertEqual(answer, correct)


class TestBishop(unittest.TestCase):
    def setUp(self):
        self.chess = Chessercise()

    def test_corner(self):
        correct = ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8']
        answer = self.chess.calc_bishop((0, 0))
        answer.sort()
        self.assertEqual(answer, correct)

    def test_middles(self):
        correct = ['a6', 'b1', 'b5', 'c2', 'c4', 'e2', 'e4', 'f1', 'f5', 'g6', 'h7']
        answer = self.chess.calc_bishop((3, 2))
        answer.sort()
        self.assertEqual(answer, correct)


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.chess = Chessercise()

    def test_corner(self):
        correct = ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'c1', 'c3',
                   'd1', 'd4', 'e1', 'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8']
        answer = self.chess.calc_queen((0, 0))
        answer.sort()
        self.assertEqual(answer, correct)

    def test_middle(self):
        correct = ['a3', 'a6', 'b1', 'b3', 'b5', 'c2', 'c3', 'c4', 'd1', 'd2', 'd4', 'd5', 'd6',
                   'd7', 'd8', 'e2', 'e3', 'e4', 'f1', 'f3', 'f5', 'g3', 'g6', 'h3', 'h7']
        answer = self.chess.calc_queen((3, 2))
        answer.sort()
        self.assertEqual(answer, correct)


if __name__ == '__main__':
    unittest.main()
