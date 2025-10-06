import sys
from collections import deque

input = sys.stdin.readline
h, w, p = map(int, input().split())
s = list(map(int, input().split()))
board = [list(input()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
score = [0] * (p + 1)
dq_list = [deque() for _ in range(p + 1)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(1, p + 1):
    for y in range(h):
        for x in range(w):
            if board[y][x] == str(i):
                score[i] += 1
                visited[y][x] = True
                dq_list[i].append((x, y))


def bfs(x, y, player_number):
    dq = []

    for d in directions:
        dx, dy = x + d[0], y + d[1]
        if not (0 <= dx < w and 0 <= dy < h):
            continue
        if visited[dy][dx] or board[dy][dx] == "#":
            continue
        visited[dy][dx] = True
        dq.append((dx, dy))
        score[player_number] += 1

    return dq


turn = 0
while True:
    turn = turn % p + 1

    for _ in range(s[turn - 1]):
        dq = []
        for pos in dq_list[turn]:
            dq.extend(bfs(pos[0], pos[1], turn))
        dq_list[turn] = deque(dq)

    if not any(bool(dq) for dq in dq_list):
        break

print(" ".join(map(str, score[1:])))
