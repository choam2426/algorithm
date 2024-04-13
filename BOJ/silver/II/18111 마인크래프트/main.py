board = []
height, time = 0, 100000000
N, M, B = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(257):
    tmp_time = 0
    block = B
    for z in range(N):
        for x in range(M):
            y = board[z][x]
            diff = i - y
            if diff < 0:
                diff *= -1
                tmp_time += 2 * diff
                block += diff
            elif diff > 0:
                tmp_time += diff
                block -= diff
            else:
                continue
    if block < 0:
        break
    if tmp_time <= time:
        time = tmp_time
        height = i

print(time, height)
