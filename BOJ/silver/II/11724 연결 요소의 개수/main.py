# https://www.acmicpc.net/problem/11724
from collections import deque

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
visited = [False] * (n + 1)
result = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    visited[i] = True
    dq = deque([i])
    while dq:
        node = dq.popleft()

        for d, v in enumerate(graph[node]):
            if v == 0:
                continue
            if not visited[d]:
                dq.append(d)
                visited[d] = True
    result += 1
print(result)
