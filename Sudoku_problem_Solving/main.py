import random
from sudoku_csp import SudokuCSP

def generate_random_sudoku(empty_cells=50):
    """
    Crée une grille valide en résolvant un Sudoku vide puis en supprimant des cases.
    """
    csp = SudokuCSP([[0]*9 for _ in range(9)])
    solution = csp.solve()
    if not solution:
        raise Exception("Impossible de générer un Sudoku valide.")

    # Convertir en grille
    full_grid = [[solution[(r, c)] for c in range(9)] for r in range(9)]

    # Enlever aléatoirement des cases
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)
    for i in range(empty_cells):
        r, c = positions[i]
        full_grid[r][c] = 0

    return full_grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(val) if val != 0 else '.' for val in row))

def main():
    print("🔢 Grille Sudoku générée aléatoirement :")
    grid = generate_random_sudoku()
    print_grid(grid)

    csp = SudokuCSP(grid)
    solution = csp.solve()

    if solution:
        print("\n✅ Solution trouvée :")
        solved_grid = [[solution[(r, c)] for c in range(9)] for r in range(9)]
        print_grid(solved_grid)
    else:
        print("\n❌ Aucune solution trouvée.")

if __name__ == "__main__":
    main()
