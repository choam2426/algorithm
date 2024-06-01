from collections import deque

vector = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
T = int(input())


def get_turn(l: int):
    visit = [[0] * l for _ in range(l)]
    dq = deque()
    sy, sx = map(int, input().split())
    visit[sy][sx] = 1
    dq.append((sy, sx, 0))
    ty, tx = map(int, input().split())
    while dq:
        y, x, turn = dq.popleft()

        if y == ty and x == tx:
            print(turn)
            break

        for v in vector:
            dy = y + v[0]
            dx = x + v[1]

            if not (0 <= dy < l and 0 <= dx < l) or visit[dy][dx]:
                continue

            dq.append((dy, dx, turn + 1))
            visit[dy][dx] = 1


for _ in range(T):
    l = int(input())
    get_turn(l)
