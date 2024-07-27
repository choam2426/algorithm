from collections import deque


def move(pos, time):
    yield pos - 1, time + 1
    yield pos + 1, time + 1


N, K = map(int, input().split())

if N > K or N == K:
    print(N - K)
    exit(0)

visit = [False] * 100001
dq = deque()
visit[N] = True
dq.append((N, 0))
while dq:
    pos, time = dq.popleft()
    d_pos = pos * 2
    while 0 < d_pos < 100001:
        if d_pos == K:
            print(time)
            exit(0)
        if visit[d_pos] == True:
            break
        dq.append((d_pos, time))
        visit[d_pos] = True
        d_pos *= 2

    for d_pos, d_time in move(pos, time):
        if d_pos == K:
            print(d_time)
            exit(0)
        if 0 <= d_pos < 100001 and visit[d_pos] == False:
            visit[d_pos] = True
            dq.append((d_pos, d_time))
