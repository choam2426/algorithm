from collections import deque

R, C = map(int, input().split())
miro = [list(input()) for _ in range(R)]
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dq = deque()
escape_flag = False

# 지훈, 불 위치 찾기
for y in range(R):
    for x in range(C):
        if miro[y][x] == "F":
            dq.appendleft((y, x, miro[y][x], 1))
        elif miro[y][x] == "J":
            dq.append((y, x, miro[y][x], 1))

while dq:
    y, x, obj_type, turn = dq.popleft()
    if (y in [R - 1, 0] or x in [C - 1, 0]) and obj_type == "J":
        escape_flag = True
        break
    for v in vectors:
        dy = y + v[0]
        dx = x + v[1]
        if (0 <= dy < R) and (0 <= dx < C) and miro[dy][dx] != "#":
            if obj_type == "F" and miro[dy][dx] != "F":
                miro[dy][dx] = "F"
                dq.append((dy, dx, "F", turn + 1))
            elif miro[dy][dx] == ".":
                miro[dy][dx] = "J"
                dq.append((dy, dx, "J", turn + 1))

if escape_flag:
    print(turn)
else:
    print("IMPOSSIBLE")
