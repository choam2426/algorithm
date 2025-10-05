# https://www.acmicpc.net/problem/14503
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [input().split() for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
while True:
    if room[r][c] == "0":
        result += 1
        room[r][c] = "2"

    if all([room[r + dx][c + dy] != "0" for dx, dy in directions]):
        r, c = r + directions[d - 2][0], c + directions[d - 2][1]
        if room[r][c] == "1":
            break
        continue
    d = (4 + d - 1) % 4
    r, c = r + directions[d][0], c + directions[d][1]
    if room[r][c] == "0":
        continue
    r, c = r + directions[d - 2][0], c + directions[d - 2][1]


print(result)
