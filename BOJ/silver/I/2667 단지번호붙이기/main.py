from collections import deque

N = int(input())

board = []
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(N):
    board.append(list(input()))

result = []
dq = deque()
for y in range(N):
    for x in range(N):
        area = 0

        if board[y][x] == "0":
            continue

        dq.append((y, x))
        board[y][x] = "0"
        area += 1

        while dq:
            ny, nx = dq.popleft()

            for v in vectors:
                dy, dx = ny + v[0], nx + v[1]
                if (0 <= dy < N) and (0 <= dx < N) and board[dy][dx] == "1":
                    area += 1
                    board[dy][dx] = "0"
                    dq.append((dy, dx))

        if area:
            result.append(area)
print(len(result))
for i in sorted(result):
    print(i)
