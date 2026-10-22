EMPTY = " "

class Board:
    def __init__(self, size=3):
        if size < 3:
            raise ValueError("Size cannot be less than 3!")
        self._size = size
        self._grid = [[EMPTY] * self.size for _ in range(self.size)]


    @property
    def size(self):
        return self._size


    def cell(self, row, col):
        """Return the mark at a cell"""
        if self._in_range(row, col):
            return self._grid[row][col]
        return None
    
    
    def _in_range(self, row, col):
        """Checks if a (row, col) is within bounds of the board"""
        return (0 <= row < self.size) and (0 <= col < self.size)


    def place_mark(self, row, col, mark):
        """Returns True if we can place a mark on the given (row, col), and False otherwise."""
        if not self._in_range(row, col):
            return False

        if self.cell(row, col) != EMPTY:
            return False

        self._grid[row][col] = mark
        return True
    

    def empty_cells(self):
        """Returns a list of [(row, col)] which don't have a mark placed on them."""
        res = []
        for r in range(self.size):
            for c in range(self.size):
                if self.cell(r, c) == EMPTY:
                    res.append((r, c))

        return res


    def is_full(self):
        """Returns True if the board is full, False otherwise."""
        return not self.empty_cells()
    

    def copy(self):
        """Returns a clone of the current board"""
        clone = Board(self._size)
        clone._grid = [ row[:] for row in self._grid ]
        return clone


    def remove_mark(self, row, col):
        """Removes a mark placed (row, col)."""
        if self.cell(row, col):
            self._grid[row][col] = EMPTY


    def has_won(self, mark):
        """Return True if mark fills a whole row, column, or diagonal."""
        for row in self._grid:
            if all(cell == mark for cell in row):
                return True
        for col in range(self.size):
            if all(self._grid[row][col] == mark for row in range(self.size)):
                return True
        if all(self._grid[i][i] == mark for i in range(self.size)):
            return True
        return all(self._grid[i][self.size - 1 - i] == mark for i in range(self.size))


    def __str__(self):
        """Prints the board in the command line."""
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)