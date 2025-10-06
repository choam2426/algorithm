import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
switches = [[[] for _ in range(n)] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
board = [[False] * n for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switches[y - 1][x - 1].append((a - 1, b - 1))

visited[0][0] = True
board[0][0] = True
dq = deque([(0, 0)])
result = 1
while dq:
    x, y = dq.popleft()

    for tx, ty in switches[y][x]:
        if board[ty][tx]:
            continue
        board[ty][tx] = True
        result += 1
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = tx + d[0], ty + d[1]
            if 0 <= dx < n and 0 <= dy < n and visited[dy][dx]:
                dq.append((dx, dy))

    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < n and 0 <= dy < n and board[dy][dx] and not visited[dy][dx]:
            dq.append((dx, dy))
            visited[dy][dx] = True
print(result)
