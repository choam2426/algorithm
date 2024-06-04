from collections import deque

M, N, K = map(int, input().split())
# n = x m = y
board = [[0] * N for _ in range(M)]
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(K):
    quad = list(map(int, input().split()))
    for y in range(quad[1], quad[3]):
        for x in range(quad[0], quad[2]):
            board[y][x] = 1

result = []
dq = deque()
for y in range(M):
    for x in range(N):
        area = 0

        if board[y][x]:
            continue

        dq.append((y, x))
        board[y][x] = 1
        area += 1

        while dq:
            ny, nx = dq.popleft()

            for v in vectors:
                dy, dx = ny + v[0], nx + v[1]
                if (0 <= dy < M) and (0 <= dx < N) and board[dy][dx] == 0:
                    area += 1
                    board[dy][dx] = 1
                    dq.append((dy, dx))

        if area:
            result.append(area)
print(len(result))
print(*sorted(result))
