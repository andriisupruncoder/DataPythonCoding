import random

N = 9
M = 20  # Number of clues. The fewer clues, the tougher the problem. You can adjust this for varying difficulty.

base  = range(N)
pattern = [[(i*N + j) % N for j in range(N)] for i in range(N)]

def shuffle(s):
    return random.sample(s, len(s))

rBase = range(N)
rows  = [ g*M + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g*M + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums  = shuffle(range(1, N + 1))

board = [[nums[pattern[r][c]] for c in cols] for r in rows]

for i in range(N):
    for j in range(N):
        if random.randrange(N*N) > M:
            board[i][j] = 0

def print_board():
    for row in board:
        print(' '.join([(' ' if x == 0 else str(x)) for x in row]))

print_board()
