import unittest
from main import create_empty_board, place_queen

class TestPlaceQueen(unittest.TestCase):

    def test_place_queen_valid(self):
        """Test : Placer une reine dans un tableau 4x4"""
        board = create_empty_board(4)
        expected = [
            ["O", "O", "O", "O"],
            ["O", "#", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"]
        ]
        self.assertEqual(place_queen(board, 1, 1), expected)

    def test_place_queen_out_of_bounds(self):
        """Test : Placer une reine hors limites (ne doit pas modifier le plateau)"""
        board = create_empty_board(4)
        expected = [row[:] for row in board] 
        self.assertEqual(place_queen(board, -1, 2), expected) 
        self.assertEqual(place_queen(board, 4, 2), expected)  
        self.assertEqual(place_queen(board, 2, 4), expected)  
        self.assertEqual(place_queen(board, 2, -1), expected) 

if __name__ == "__main__":
    unittest.main()
