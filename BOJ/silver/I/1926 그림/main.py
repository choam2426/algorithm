from collections import deque

N, M = map(int, input().split())
visit_board = [[0] * M for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
count = 0
result = 0
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dq = deque()

for y in range(N):
    for x in range(M):
        tmp = 1
        if visit_board[y][x]:
            continue
        visit_board[y][x] = 1
        if not board[y][x]:
            continue
        dq.append((y, x))
        while dq:
            ny, nx = dq.popleft()
            for v in vector:
                dy = ny + v[0]
                dx = nx + v[1]
                if not ((0 <= dy < N) and (0 <= dx < M)):
                    continue
                if board[dy][dx] and (not visit_board[dy][dx]):
                    dq.append((dy, dx))
                    tmp += 1
                visit_board[dy][dx] = 1

        if result < tmp:
            result = tmp
        count += 1
print(count, result)
