from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit_board = [[0] * M for _ in range(N)]
vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dq = deque()

# 시작 지점 확인
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            visit_board[y][x] = 1
            dq.append((y, x, 0))
        if board[y][x] == -1:
            visit_board[y][x] = 1

# BFS
while dq:
    y, x, day = dq.popleft()

    for v in vectors:
        ny = y + v[0]
        nx = x + v[1]

        if (0 <= ny < N) and (0 <= nx < M) and visit_board[ny][nx] == 0:
            visit_board[ny][nx] = 1
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                dq.append((ny, nx, day + 1))

# 안익은 토마토 확인
for y in range(N):
    if 0 in board[y]:
        print(-1)
        break
else:
    print(day)
