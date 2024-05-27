from collections import deque

N = int(input())
picture = [list(input()) for _ in range(N)]
visit = [[[False] * N for _ in range(N)] for _ in range(2)]
result = [0, 0]
dq = deque()
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check_range(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    else:
        return False


def check_color(y, x, now_color, eye_type):
    color = picture[y][x]

    if eye_type == 1:
        if now_color in ["R", "G"] and color == "B":
            return False
        elif now_color == "B" and color in ["R", "G"]:
            return False
    else:
        if color != now_color:
            return False
    return True


for y in range(N):
    for x in range(N):
        now_color = picture[y][x]
        for z in range(2):
            if visit[z][y][x]:
                continue
            dq.append((y, x))
            visit[z][y][x] = True
            result[z] += 1
            while dq:
                ny, nx = dq.popleft()
                for v in vectors:
                    dy = ny + v[0]
                    dx = nx + v[1]
                    if check_range(dy, dx) == False or visit[z][dy][dx]:
                        continue
                    if check_color(dy, dx, now_color, z):
                        dq.append((dy, dx))
                        visit[z][dy][dx] = True
print(*result)
