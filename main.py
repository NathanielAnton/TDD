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

    empty_board = create_empty_board(n)
    print_board(empty_board)
