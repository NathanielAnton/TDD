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

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "#":
            return False
        i += 1
        j -= 1

    i, j = row, col
    while i < n and j < n:
        if board[i][j] == "#":
            return False
        i += 1
        j += 1

    return True

def solve_n_queens(n: int) -> List[List[str]]:
    if n <= 0:
        return [] 

    solutions = []  

    def backtrack(row: int, board: List[List[str]]):
        if row == n:
            solutions.append(["".join(line) for line in board])  
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                new_board = [line[:] for line in board]  
                new_board = place_queen(new_board, row, col) 
                backtrack(row + 1, new_board) 

    empty_board = create_empty_board(n)
    backtrack(0, empty_board)
    return solutions

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print("".join(row))
    print()

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Entrez la taille du tableau (N) : "))
            if n < 0:
                print("Veuillez entrer un nombre positif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    solutions = solve_n_queens(n)

    if not solutions:
        print(f"Aucune solution trouvée pour N={n}.")
    else:
        print(f"{len(solutions)} solution(s) trouvée(s) pour N={n} :\n")
        for index, board in enumerate(solutions, start=1):
            print(f"Solution {index}:")
            print_board(board)

