__author__ = 'Stuart Glassett'

"""
Write a program that will accept two command line parameters:
    1. Type of chess piece (Queen, Rook, Knight)
    2. Current position on a chess board
Return:
    A list of all the potential board positions the given piece could advance to, with one move, from the given position
"""
import argparse
from itertools import chain


class Chessercise:
    """
    Class to hold the board layout and methods to calculate paths
    """

    board = (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ['1', '2', '3', '4', '5', '6', '7', '8'])

    def text_to_position(self, text):
        """
        Convert text position (ie, 'd2') to a position tuple, in this case (3, 1)
        :param text: text position
        :return: position tuple
        """
        # Check for invalid board positions
        if text[0] not in self.board[0] or text[1] not in self.board[1]:
            print("You have entered an invalid chess board location\n"
                  "Valid locations are a1 through h8")
            return

        return self.board[0].index(text[0]), self.board[1].index(text[1])

    def calc_knight(self, position):
        """
        Knight has a max of 8 possible moves in a specific pattern
        :param position: current position of piece in tuple of board indexes
        :return: list of possible moves
        """
        # All of the possible routes a knight can take
        routes = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        valid_moves = []

        # Iterate through the valid routes and generate the board positions
        for route in routes:
            x = position[0] + route[0]
            y = position[1] + route[1]
            if 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append(self.board[0][x] + self.board[1][y])

        return valid_moves

    def calc_bishop(self, position):
        """
        Bishop can only move diagonally but is unconstrained in distance
        :param position: current position of piece in tuple of board indexes
        :return: list of possible moves
        """
        # Create possible locations on the board, can't be in same row or column it started
        xpos = self.board[0][position[0] + 1:]
        xneg = self.board[0][:position[0]]
        ypos = self.board[1][position[1] + 1:]
        yneg = self.board[1][:position[1]]

        # Need to reverse the 'negative' positions
        xneg.reverse()
        yneg.reverse()

        # Chain the combinations of the lists, dropping any null values, return the concatenation of the tuple values
        return [x + y for (x, y) in chain(zip(xpos, ypos), zip(xpos, yneg), zip(xneg, ypos), zip(xneg, yneg))]

    def calc_rook(self, position):
        """
        Rook can only move vertically and horizontally but is unconstrained in distance
        :param position: current position of piece in tuple of board indexes
        :return: list of possible moves
        """
        valid_moves = []
        # Iterate through the column and row adding each square that isn't the currently occupied square
        for x in self.board[0]:
            if x != self.board[0][position[0]]:
                valid_moves.append(x + self.board[1][position[1]])
        for y in self.board[1]:
            if y != self.board[1][position[1]]:
                valid_moves.append(self.board[0][position[0]] + y)
        return valid_moves

    def calc_queen(self, position):
        """
        Queen can move in any linear direction, unconstrained in distance, effectively the union of rook and bishop
        :param position: current position of piece in tuple of board indexes
        :return: combination of the lists returned by calc_bishop and calc_rook
        """
        return self.calc_bishop(position) + self.calc_rook(position)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A chess piece move calculator")
    parser.add_argument("-piece", required=True, choices=["knight", "rook", "bishop", "queen"], type=str)
    parser.add_argument("-position", required=True, type=str, help="Chess board position of the piece (ie d4)")
    args = parser.parse_args()

    # Initialize the class as well as an empty result set
    chess = Chessercise()
    result = []

    # Convert the given position into a tuple of list indexes
    pos = chess.text_to_position(args.position)

    # If a valid position was entered, pass the position to the correct function for the piece
    if pos is not None:
        if args.piece == "knight":
            result = chess.calc_knight(pos)
        elif args.piece == "rook":
            result = chess.calc_rook(pos)
        elif args.piece == "bishop":
            result = chess.calc_bishop(pos)
        elif args.piece == "queen":
            result = chess.calc_queen(pos)

        # Sort the end results for slightly nicer printing and then print
        result.sort()
        print(str(result).strip('[]'))
