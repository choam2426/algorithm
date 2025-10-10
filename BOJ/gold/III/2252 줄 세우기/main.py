# https://www.acmicpc.net/problem/2252
from collections import deque

n, m = map(int, input().split())
deg = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    deg[v] += 1
    graph[u].append(v)

dq = deque([i for i in range(1, n + 1) if deg[i] == 0])
while dq:
    node = dq.popleft()
    print(node, end=" ")

    for child in graph[node]:
        deg[child] -= 1
        if deg[child] == 0:
            dq.append(child)
