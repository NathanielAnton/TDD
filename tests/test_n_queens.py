import unittest
from main import solve_n_queens

class TestNQueens(unittest.TestCase):

    def test_n_queens_4(self):
        """Test du problème des N-Queens avec N=4"""
        expected = [
            [
                "O#OO",
                "OOO#",
                "#OOO",
                "OO#O"
            ],
            [
                "OO#O",
                "#OOO",
                "OOO#",
                "O#OO"
            ]
        ]
        self.assertCountEqual(solve_n_queens(4), expected)

    def test_n_queens_0(self):
        """Test du problème avec N=0 (aucune solution)"""
        expected = []
        self.assertEqual(solve_n_queens(0), expected)

    def test_n_queens_1(self):
        """Test du problème avec N=1"""
        expected = [["#"]]
        self.assertEqual(solve_n_queens(1), expected)

    def test_n_queens_2(self):
        """Test du problème avec N=2 (aucune solution possible)"""
        expected = []
        self.assertEqual(solve_n_queens(2), expected)

    def test_n_queens_3(self):
        """Test du problème avec N=3 (aucune solution possible)"""
        expected = []
        self.assertEqual(solve_n_queens(3), expected)

if __name__ == "__main__":
    unittest.main()
