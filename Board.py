class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[(-1, -1) for c in range(cols)] for r in range(rows)]

    def __repr__(self):
        for row in range(self.rows):
            print(*['X' if self.square_is_visited(row, col) else 'O' for col in range(self.rows)], sep=' ')

    def get_square(self, r, c):
        return self.board[r][c]

    def set_parent(self, r, c, pr, pc):
        self.board[r][c] = (pr, pc)
    
    def square_is_visited(self, r, c):
        return self.board[r][c] != (-1, -1)

    def is_valid_coor(self, r, c):
        return 0 <= r and r < self.rows and 0 <= c and c < self.cols
    
    def all_visited(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.square_is_visited(r, c):
                    return False
        return True
