from collections import deque
from copy import deepcopy

N = int(input())

board = []
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
rain = 0
dq = deque()
while True:
    area = 0
    rain += 1
    new_board = deepcopy(board)
    for y in range(N):
        for x in range(N):

            if new_board[y][x] < rain:
                continue

            dq.append((y, x))
            new_board[y][x] = 0
            area += 1

            while dq:
                ny, nx = dq.popleft()

                for v in vectors:
                    dy, dx = ny + v[0], nx + v[1]
                    if (0 <= dy < N) and (0 <= dx < N) and new_board[dy][dx] >= rain:
                        new_board[dy][dx] = 0
                        dq.append((dy, dx))
    if area > result:
        result = area
    if area == 0:
        break


print(result)
