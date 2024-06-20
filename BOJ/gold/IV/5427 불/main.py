from collections import deque

vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    miro = [list(input()) for _ in range(H)]
    dq = deque()
    escape_flag = False

    # 지훈, 불 위치 찾기
    for y in range(H):
        for x in range(W):
            if miro[y][x] == "@":
                dq.append((y, x, miro[y][x], 1))
            elif miro[y][x] == "*":
                dq.appendleft((y, x, miro[y][x], 1))

    while dq:
        y, x, obj_type, turn = dq.popleft()
        if (y in [H - 1, 0] or x in [W - 1, 0]) and obj_type == "@":
            escape_flag = True
            break
        for v in vectors:
            dy = y + v[0]
            dx = x + v[1]
            if (0 <= dy < H) and (0 <= dx < W):
                if obj_type == "*" and miro[dy][dx] in [".", "@"]:
                    miro[dy][dx] = "*"
                    dq.append((dy, dx, "*", turn + 1))
                elif obj_type == "@" and miro[dy][dx] == ".":
                    miro[dy][dx] = "@"
                    dq.append((dy, dx, "@", turn + 1))

    if escape_flag:
        print(turn)
    else:
        print("IMPOSSIBLE")
