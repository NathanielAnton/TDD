import unittest
from typing import List
from main import create_empty_board

class TestBoardCreation(unittest.TestCase):
    
    def test_size_4(self):
        """Test avec un tableau 4x4"""
        expected = [
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"]
        ]
        self.assertEqual(create_empty_board(4), expected)

    def test_size_1(self):
        """Test avec un tableau 1x1"""
        expected = [["O"]]
        self.assertEqual(create_empty_board(1), expected)

    def test_size_0(self):
        """Test avec un tableau 0x0 (doit être une liste vide)"""
        expected: List[List[str]] = []
        self.assertEqual(create_empty_board(0), expected)

    def test_size_negative(self):
        """Test avec un nombre négatif (doit être une liste vide)"""
        expected: List[List[str]] = []
        self.assertEqual(create_empty_board(-3), expected)

    def test_non_integer_values(self):
        """Test avec des valeurs non entières (devrait retourner une liste vide)"""
        expected: List[List[str]] = []
        self.assertEqual(create_empty_board("4"), expected)
        self.assertEqual(create_empty_board(4.5), expected)
        self.assertEqual(create_empty_board(None), expected)
        self.assertEqual(create_empty_board([]), expected)
        self.assertEqual(create_empty_board({}), expected)

if __name__ == "__main__":
    unittest.main()
