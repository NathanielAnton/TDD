import unittest
from main import is_safe, create_empty_board, place_queen

class TestIsSafe(unittest.TestCase):

    def test_no_conflict(self):
        """Test : Aucune reine ne bloque la position"""
        board = create_empty_board(4)
        board = place_queen(board, 0, 0)  
        expected = True  
        result = is_safe(board, 2, 3, 4)
        self.assertEqual(result, expected)

    def test_conflict_same_column(self):
        """Test : Une reine est déjà dans la même colonne"""
        board = create_empty_board(4)
        board = place_queen(board, 0, 2) 
        expected = False 
        result = is_safe(board, 2, 2, 4)
        self.assertEqual(result, expected)

    def test_conflict_diagonal_top_left(self):
        """Test : Une reine est sur la diagonale haut-gauche"""
        board = create_empty_board(4)
        board = place_queen(board, 1, 1)  
        expected = False 
        result = is_safe(board, 2, 2, 4)
        self.assertEqual(result, expected)

    def test_conflict_diagonal_top_right(self):
        """Test : Une reine est sur la diagonale haut-droite"""
        board = create_empty_board(4)
        board = place_queen(board, 1, 3) 
        expected = False 
        result = is_safe(board, 2, 2, 4)
        self.assertEqual(result, expected)

    def test_conflict_diagonal_bottom_left(self):
        """Test : Une reine est sur la diagonale bas-gauche"""
        board = create_empty_board(4)
        board = place_queen(board, 3, 0) 
        expected = False 
        result = is_safe(board, 2, 1, 4)
        self.assertEqual(result, expected)

    def test_conflict_diagonal_bottom_right(self):
        """Test : Une reine est sur la diagonale bas-droite"""
        board = create_empty_board(4)
        board = place_queen(board, 3, 3)
        expected = False  
        result = is_safe(board, 2, 2, 4)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
