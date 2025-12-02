from Board import Board

# clockwise, starting UR
MOVES = [
    (-2, 1), (-1, 2), (1, 2), (2, 1), 
    (2, -1), (1, -2), (-1, -2), (-2, -1)
]

def rec(board, r, c, depth):
    # print(" "*depth, r, c)
    no_moves = True
    for dr, dc in MOVES:
        nr = r + dr
        nc = c + dc
        if board.is_valid_coor(nr, nc) and not board.square_is_visited(nr, nc):
            no_moves = False
            board.set_parent(nr, nc, r, c)
            rec(board, nr, nc, depth+1)
            board.set_parent(nr, nc, -1, -1)
    
    if no_moves:
        if board.all_visited():
            last[r][c] += 1


if __name__ == "__main__":
    ROWS = 5
    COLS = 5
    board = Board(ROWS, COLS)
    board.set_parent(0,0,0,0)
    last = [[0 for j in range(COLS)] for i in range(ROWS)]
    rec(board, 0, 0, 0)
    
    for row in last:
        print(row)

    