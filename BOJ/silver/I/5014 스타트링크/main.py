from collections import deque

F, S, G, U, D = map(int, input().split())
dq = deque([(S, 0)])
visit = [False] * (F + 1)

while True:
    if not dq:
        button = "use the stairs"
        break
    pos, button = dq.popleft()
    if pos == G:
        break

    for dpos in [pos + U, pos - D]:

        if 0 < dpos < F + 1 and visit[dpos] == False:

            dq.append((dpos, button + 1))
            visit[dpos] = True
print(button)
