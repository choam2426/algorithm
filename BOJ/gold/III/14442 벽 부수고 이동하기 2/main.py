# https://www.acmicpc.net/problem/14442
from collections import deque

n, m, k = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
dq = deque([(0, 0, k, 1)])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while dq:
    x, y, k, t = dq.popleft()

    if x == m - 1 and y == n - 1:
        print(t)
        break

    for d in directions:
        dx, dy = x + d[0], y + d[1]

        if not (0 <= dx < m and 0 <= dy < n):
            continue

        if board[dy][dx] == "1" and k > 0:
            if not visited[dy][dx][k - 1]:
                dq.append((dx, dy, k - 1, t + 1))
                visited[dy][dx][k - 1] = True

        if board[dy][dx] == "0":
            if not visited[dy][dx][k]:
                dq.append((dx, dy, k, t + 1))
                visited[dy][dx][k] = True
else:
    print(-1)
