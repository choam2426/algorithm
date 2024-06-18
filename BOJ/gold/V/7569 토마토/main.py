from collections import deque

vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N, H = map(int, input().split())


box = []
dq = deque()
for z in range(H):
    l = []
    for y in range(N):
        line = list(map(int, input().split()))
        l.append(line)
    box.append(l)

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                dq.append((z, y, x, 0))

time = 0
while dq:
    z, y, x, time = dq.popleft()

    for v in vectors:
        ny = y + v[0]
        nx = x + v[1]

        if (0 <= ny < N) and (0 <= nx < M) and box[z][ny][nx] == 0:
            box[z][ny][nx] = 1
            dq.append((z, ny, nx, time + 1))

    for v in [-1, 1]:
        nz = z + v

        if (0 <= nz < H) and box[nz][y][x] == 0:
            box[nz][y][x] = 1
            dq.append((nz, y, x, time + 1))

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                time = -1

print(time)
