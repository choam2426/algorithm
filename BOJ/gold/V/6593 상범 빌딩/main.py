from collections import deque

vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while True:
    L, R, C = map(int, input().split())

    if (L * R * C) == 0:
        break

    building = []
    dq = deque()
    for z in range(L):
        l = []
        for y in range(R):
            line = list(input())
            if "S" in line:
                dq.append((z, y, line.index("S"), 0))
            if "E" in line:
                escape_pos = (z, y, line.index("E"))
            l.append(line)
        input()
        building.append(l)

    pass

    while dq:
        z, y, x, time = dq.popleft()
        if (z, y, x) == escape_pos:
            print(f"Escaped in {time} minute(s).")
            break

        for v in vectors:
            ny = y + v[0]
            nx = x + v[1]

            if (0 <= ny < R) and (0 <= nx < C) and building[z][ny][nx] != "#":
                building[z][ny][nx] = "#"
                dq.append((z, ny, nx, time + 1))

        for v in [-1, 1]:
            nz = z + v

            if (0 <= nz < L) and building[nz][y][x] != "#":
                building[nz][y][x] = "#"
                dq.append((nz, y, x, time + 1))
    else:
        print("Trapped!")
