from collections import deque


def move(pos):
    yield pos - 1
    yield pos + 1
    yield pos * 2


x, goal = map(int, input().split())
dq = deque([(x, 0)])
visit = [False] * 100001
while True:
    pos, time = dq.popleft()

    if pos == goal:
        print(time)
        break

    for dpos in move(pos):
        if 0 <= dpos < 100001 and visit[dpos] == False:
            dq.append((dpos, time + 1))
            visit[dpos] = True
