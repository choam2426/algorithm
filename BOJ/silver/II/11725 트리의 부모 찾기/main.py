# https://www.acmicpc.net/problem/11725
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dq = deque([1])
while dq:
    node = dq.popleft()
    for child in graph[node]:
        if parents[child] != 0:
            continue
        parents[child] = node
        dq.append(child)

print("\n".join(map(str, parents[2:])))
