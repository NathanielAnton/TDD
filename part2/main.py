import unittest
from typing import List

def create_empty_board(n: int) -> List[List[str]]:
    if not isinstance(n, int) or n < 0:
        return []
    return [["O" for _ in range(n)] for _ in range(n)]

def place_queen(board: List[List[str]], row: int, col: int) -> List[List[str]]:
    n = len(board)
    if not (0 <= row < n and 0 <= col < n):
        return board 

    board[row][col] = "#" 
    return board

def is_attacking(r1, c1, r2, c2) -> bool:
    return r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2)

def valid_single_attack_configuration(board: List[List[str]]) -> bool:
    queens = [(r, c) for r in range(len(board)) for c in range(len(board)) if board[r][c] == "#"]
    attack_map = {q: None for q in queens}
    attacked_by = {q: None for q in queens}
    
    for q1 in queens:
        for q2 in queens:
            if q1 != q2 and is_attacking(*q1, *q2):
                if attack_map[q1] is None:
                    attack_map[q1] = q2
                else:
                    return False  
                
                if attacked_by[q2] is None:
                    attacked_by[q2] = q1
                else:
                    return False 
    
    return all(attack_map[q] is not None and attacked_by[q] is not None for q in queens)

def is_safe(board: List[List[str]], row: int, col: int, n: int) -> bool:
    for i in range(row):
        if board[i][col] == "#":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "#":
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "#":
            return False
        i -= 1
        j += 1

    return True

def find_valid_configurations(n: int) -> List[List[List[str]]]:
    solutions = []
    board = create_empty_board(n)
    
    def backtrack(queens):
        if len(queens) == n:
            board_copy = [row[:] for row in board]
            if valid_single_attack_configuration(board_copy):
                solutions.append(["".join(row) for row in board_copy])
            return
        
        row = len(queens)
        for col in range(n):
            board[row][col] = "#"
            queens.append((row, col))
            backtrack(queens)
            queens.pop()
            board[row][col] = "O"
    
    backtrack([])
    return solutions

class TestQueensProblem(unittest.TestCase):
    def test_create_empty_board(self):
        self.assertEqual(create_empty_board(3), [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']])
    
    def test_valid_single_attack_configuration(self):
        board = [
            ["#", "O", "O", "O"],
            ["O", "O", "#", "O"],
            ["#", "O", "O", "O"],
            ["O", "O", "#", "O"]
        ]
        self.assertTrue(valid_single_attack_configuration(board))
    
        invalid_board = [
            ["#", "#", "O", "O"],
            ["O", "O", "O", "#"],
            ["#", "O", "O", "O"],
            ["O", "O", "#", "O"]
        ]
        self.assertFalse(valid_single_attack_configuration(invalid_board))
    
    def test_find_valid_configurations(self):
        n = 4
        configurations = find_valid_configurations(n)
        
        for config in configurations:
            self.assertTrue(valid_single_attack_configuration(config))
        
        self.assertGreater(len(configurations), 0)

if __name__ == "__main__":
    unittest.main()
