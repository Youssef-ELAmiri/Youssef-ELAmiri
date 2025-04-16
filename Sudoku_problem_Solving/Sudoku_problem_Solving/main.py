from sudoku_csp import SudokuCSP

def print_grid(grid):
    for row in grid:
        print(" ".join(str(val) if val != 0 else '.' for val in row))

def main():
    # Grille Sudoku de l'exercice (exemple — à adapter si besoin)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print(" Grille Sudoku à résoudre :")
    print_grid(grid)

    csp = SudokuCSP(grid)
    solution = csp.solve()

    if solution:
        print("\n-->Solution trouvée :")
        solved_grid = [[solution[(r, c)] for c in range(9)] for r in range(9)]
        print_grid(solved_grid)
    else:
        print("\n--<>Aucune solution trouvée.")

if __name__ == "__main__":
    main()
