from collections import deque

vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(sea_map: list, N: int, M: int) -> int:
    visit = [[False] * M for _ in range(N)]
    dq = deque()
    result = 0
    for y in range(N):
        for x in range(M):
            if visit[y][x] or sea_map[y][x] <= 0:
                continue
            result += 1
            dq.append((y, x))
            visit[y][x] = True
            while dq:
                ny, nx = dq.popleft()

                for v in vectors:
                    dy = ny + v[0]
                    dx = nx + v[1]

                    if 0 <= dy < N and 0 <= dx < M:
                        if visit[dy][dx]:
                            continue
                        elif sea_map[dy][dx] <= 0:
                            sea_map[ny][nx] -= 1
                            continue
                        dq.append((dy, dx))
                        visit[dy][dx] = True
    return result


N, M = map(int, input().split())
sea_map = [list(map(int, input().split())) for _ in range(N)]
year = 0
while True:
    iceberg_count = bfs(sea_map, N, M)
    if iceberg_count != 1:
        break
    year += 1

if iceberg_count > 1:
    print(year)
else:
    print(0)
