# https://www.acmicpc.net/problem/2146
import sys
from collections import deque

input = sys.stdin.readline

vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


# 땅 마킹 (bfs)
def mark_island(x, y, number):
    dq = deque()
    dq.append((x, y))

    while dq:
        nx, ny = dq.popleft()
        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        board[nx][ny] = number

        for v in vector:
            dx, dy = nx + v[0], ny + v[1]
            if not (0 <= dx < n and 0 <= dy < n):
                continue
            if visited[dx][dy] or (board[dx][dy] == 0):
                continue
            dq.append((dx, dy))


# 땅 스캔
island_number = 1
for i in range(n):
    for j in range(n):
        if (board[i][j] == 1) and not visited[i][j]:
            mark_island(i, j, island_number)
            island_number += 1


def calc_distance(x, y):
    dq = deque()
    visited = [[False] * n for _ in range(n)]
    dq.append((x, y, 0))
    island_number = board[x][y]
    while dq:
        nx, ny, d = dq.popleft()
        if visited[nx][ny]:
            continue

        visited[nx][ny] = True

        for v in vector:
            dx, dy = nx + v[0], ny + v[1]
            if not (0 <= dx < n and 0 <= dy < n):
                continue
            if visited[dx][dy] or (board[dx][dy] == island_number):
                continue
            if board[dx][dy] != 0:
                return d
            dq.append((dx, dy, d + 1))
    return 1000000


result = 1000000
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            result = min(calc_distance(i, j), result)

print(result)
