from collections import deque
import copy

class SudokuCSP:
    def __init__(self, grid):
        self.variables = [(r, c) for r in range(9) for c in range(9)]
        self.domains = {var: set(range(1, 10)) for var in self.variables}
        self.neighbors = {var: set() for var in self.variables}
        self.init_domains(grid)
        self.create_constraints()

    def init_domains(self, grid):
        for r in range(9):
            for c in range(9):
                val = grid[r][c]
                if val != 0:
                    self.domains[(r, c)] = {val}

    def create_constraints(self):
        for r in range(9):
            for c in range(9):
                var = (r, c)
                for i in range(9):
                    if i != c:
                        self.neighbors[var].add((r, i))
                    if i != r:
                        self.neighbors[var].add((i, c))
                box_r, box_c = 3 * (r // 3), 3 * (c // 3)
                for i in range(box_r, box_r + 3):
                    for j in range(box_c, box_c + 3):
                        if (i, j) != var:
                            self.neighbors[var].add((i, j))

    def is_consistent(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def ac3(self):
        queue = deque([(xi, xj) for xi in self.variables for xj in self.neighbors[xi]])
        while queue:
            xi, xj = queue.popleft()
            if self.revise(xi, xj):
                if not self.domains[xi]:
                    return False
                for xk in self.neighbors[xi] - {xj}:
                    queue.append((xk, xi))
        return True

    def revise(self, xi, xj):
        revised = False
        for x in set(self.domains[xi]):
            if not any(x != y for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True
        return revised

    def select_unassigned_variable(self, assignment):
        unassigned = [v for v in self.variables if v not in assignment]
        return min(unassigned, key=lambda var: len(self.domains[var]))

    def backtrack(self, assignment):
        if len(assignment) == 81:
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in sorted(self.domains[var]):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                backup = copy.deepcopy(self.domains)
                self.domains[var] = {value}
                if self.ac3():
                    result = self.backtrack(assignment)
                    if result:
                        return result
                self.domains = backup
                del assignment[var]
        return None

    def solve(self):
        if not self.ac3():
            return None
        # Vérifie si chaque domaine a exactement une seule valeur
        if all(len(self.domains[var]) == 1 for var in self.variables):
            return {var: next(iter(self.domains[var])) for var in self.variables}
        return None

