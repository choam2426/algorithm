from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
seq = []
while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())

    seq.append(queue.popleft())

print("<" + str(seq)[1:-1] + ">")
