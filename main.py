from typing import List

def create_empty_board(n: int) -> List[List[str]]:
    if not isinstance(n, int) or n < 0:
        return []
    return [["O" for _ in range(n)] for _ in range(n)]

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
