import sys
from collections import deque

input = sys.stdin.readline
k = int(input())
n, m = map(int, input().split())
board = [input().split() for _ in range(m)]

# 3차원 visited 배열: visited[x][y][남은 말 이동 횟수]
visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
horse_directions = [
    (2, 1),
    (-2, 1),
    (2, -1),
    (-2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
]

dq = deque([(0, 0, k, 0)])
visited[0][0][k] = True

while dq:
    x, y, remain_k, turn = dq.popleft()

    if x == m - 1 and y == n - 1:
        print(turn)
        exit()

    # 일반 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < m and 0 <= ny < n):
            continue

        if visited[nx][ny][remain_k]:
            continue

        if board[nx][ny] == "1":
            continue

        visited[nx][ny][remain_k] = True
        dq.append((nx, ny, remain_k, turn + 1))

    # 말 이동
    if remain_k > 0:
        for dx, dy in horse_directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if visited[nx][ny][remain_k - 1]:
                continue

            if board[nx][ny] == "1":
                continue

            visited[nx][ny][remain_k - 1] = True
            dq.append((nx, ny, remain_k - 1, turn + 1))

print(-1)
