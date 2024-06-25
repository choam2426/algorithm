from collections import deque

vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dq = deque([(0, 0, 0, 1)])

while dq:
    y, x, chance, distance = dq.popleft()

    if y == N - 1 and x == M - 1:
        print(distance)
        break

    for v in vectors:
        dy = v[0] + y
        dx = v[1] + x

        if 0 <= dy < N and 0 <= dx < M:
            if board[dy][dx] == "1" and chance == 0:
                dq.append((dy, dx, 1, distance + 1))
                visit[dy][dx][1] = 1
            elif board[dy][dx] == "0" and visit[dy][dx][chance] == 0:
                dq.append((dy, dx, chance, distance + 1))
                visit[dy][dx][chance] = 1
else:
    print(-1)
