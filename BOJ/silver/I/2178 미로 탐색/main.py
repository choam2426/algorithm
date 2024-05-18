from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit_board = [[0] * M for _ in range(N)]
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dq = deque([(0, 0, 1)])

while dq:
    y, x, dist = dq.popleft()
    visit_board[y][x] = 1
    if y == N - 1 and x == M - 1:
        break
    for v in vectors:
        ny = y + v[0]
        nx = x + v[1]
        if (0 <= ny < N) and (0 <= nx < M) and visit_board[ny][nx] == 0:
            visit_board[ny][nx] = 1
            if board[ny][nx] == "1":
                dq.append((ny, nx, dist + 1))


print(dist)
