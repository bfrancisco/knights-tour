from timeit import timeit

R, C = 8, 8
DIRS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
MX = 10

def valid(r, c):
    return 0 <= r and r < R and 0 <= c and c < C

def initialize_prio(board):
    for r in range(R):
        for c in range(C):
            valids = 0
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if valid(nr, nc): valids += 1
            board[r][c] = valids
            

def solve_util(board, prior, r, c, num):
    # print(r, c)
    if num == R*C+1:
        return True

    move_prio = [] # less prio, earlier in dir order
    for k in range(len(DIRS)):
        dr, dc = DIRS[k] 
        nr, nc = r + dr, c + dc
        if valid(nr, nc) and board[nr][nc] == -1:
            move_prio.append((k, prior[nr][nc]))

    if len(move_prio) == 0:
        return False

    move_prio.sort(key=lambda m: (m[1], m[0]))

    for k, prior_val in move_prio:
        dr, dc = DIRS[k]
        nr, nc = r + dr, c + dc
        board[nr][nc] = num
        prev_prio = prior[nr][nc]
        prior[nr][nc] = MX
        for _k in range(len(DIRS)):
            nnr, nnc = nr + DIRS[_k][0], nc + DIRS[_k][1]
            if valid(nnr, nnc) and board[nnr][nnc] == -1:
                prior[nnr][nnc] -= 1
        
        done = solve_util(board, prior, nr, nc, num+1)
        if done: return True

        board[nr][nc] = -1
        prior[nr][nc] = prev_prio
        for _k in range(len(DIRS)):
            nnr, nnc = nr + DIRS[_k][0], nc + DIRS[_k][1]
            if valid(nnr, nnc) and board[nnr][nnc] == -1:
                prior[nnr][nnc] += 1

def solve(board, prior, start_r, start_c):
    board[start_r][start_c] = 1
    prior[start_r][start_c] = MX
    for _k in range(len(DIRS)):
        nnr, nnc = start_r + DIRS[_k][0], start_c + DIRS[_k][1]
        if valid(nnr, nnc) and board[nnr][nnc] == -1:
            prior[nnr][nnc] -= 1
    solve_util(board, prior, start_r, start_c, 2)

def print_board(board):
    max_width = max(len(str(val)) for row in board for val in row) + 2
    for row in board:
        print("".join(f"{val:^{max_width}}" for val in row))

def benchmark_function(name: str) -> None:
    number = 100
    res = timeit(f"{name}", number=number, globals=globals())
    print(f"{name} finished {number} runs in {res:.5f} seconds")

if __name__ == "__main__":
    board = [[-1 for c in range(C)] for r in range(R)]
    prior = [[-1 for c in range(C)] for r in range(R)]
    initialize_prio(prior)

    solve(board, prior, 0, 0)
    print_board(prior)
    print()
    print_board(board)
    
    benchmark_function("solve(board, prior, 0, 0)")