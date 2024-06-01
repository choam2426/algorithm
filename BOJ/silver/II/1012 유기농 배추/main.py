from collections import deque

dq = deque()
vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for _ in range(T):
    M, N, cabbage = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    visit_field = [[False] * M for _ in range(N)]
    result = 0

    for _ in range(cabbage):
        x, y = map(int, input().split())
        field[y][x] = 1

    for y in range(N):
        for x in range(M):
            if field[y][x] == 0 or visit_field[y][x]:
                visit_field[y][x] = True
                continue
            visit_field[y][x] = True
            dq.append((y, x))
            while dq:
                ny, nx = dq.popleft()0
                for v in vectors:
                    dy = ny + v[0]
                    dx = nx + v[1]
                    if (0 <= dy < N) and (0 <= dx < M):
                        if not visit_field[dy][dx] and field[dy][dx] == 1:
                            visit_field[dy][dx] = True
                            dq.append((dy, dx))
            result += 1

    print(result)
