# https://www.acmicpc.net/problem/13913
from collections import deque

n, k = map(int, input().split())
line = [-1] * 100001
line[n] = n
dq = deque([n])
while True:
    pos = dq.popleft()

    if pos == k:
        break

    for dpos in [pos + 1, pos - 1, pos * 2]:
        if not 0 <= dpos < 100001:
            continue
        if line[dpos] == -1:
            line[dpos] = pos
        else:
            continue
        dq.append(dpos)

track = deque([k])
pos = line[k]
while True:
    if pos == n:
        break
    track.appendleft(pos)
    pos = line[pos]
track.appendleft(n)
track = set(track)
print(len(track) - 1)
print(" ".join(map(str, track)))
