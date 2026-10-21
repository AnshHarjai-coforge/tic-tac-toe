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
        return self._grid[row][col]
    
    
    def _in_range(self, row, col):
        return (0 <= row < self.size) and (0 <= col < self.size)


    def place_mark(self, row, col, mark):
        if not self._in_range(row, col):
            return False

        if self.cell(row, col) != EMPTY:
            return False

        self._grid[row][col] = mark
        return True
    

    def empty_cells(self):
        res = []
        for r in range(self.size):
            for c in range(self.size):
                if self.cell(r, c) == EMPTY:
                    res.append((r, c))

        return res


    def is_full(self):
        if self.empty_cells():
            return True
        return False
    

    def copy(self):
        clone = Board(self._size)
        clone._grid = [ row[:] for row in self._grid ]
        return clone


    def __str__(self):
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)


if __name__ == "__main__":

    board = Board(3)
    print(board.place_mark(0, 0, "X"))     # True
    print(board.place_mark(0, 0, "O"))     # False, the cell is taken
    print(board.place_mark(3, 0, "O"))     # False, off the board
    print(board.place_mark(-1, 0, "O"))    # False, rejected
    board.place_mark(1, 1, "O")

    print(board)
    print(len(board.empty_cells()))        # 7
