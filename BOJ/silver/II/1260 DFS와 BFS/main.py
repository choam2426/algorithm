N, M, V = map(int, input().split())
graph = {}

for i in range(N):
    graph[i] = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1] = graph.get(n1, []) + [n2]
    graph[n2] = graph.get(n2, []) + [n1]

for data in graph:
    graph[data].sort()

# DFS
stack = [V]
visit = [False] * (N + 1)
visit[V] = True
result = [V]
while stack:
    node = stack[-1]
    for i in graph[node]:
        if visit[i] == False:
            visit[i] = True
            stack.append(i)
            result.append(i)
            break
    else:
        stack.pop()
print(*result)

# BFS
q = [V]
visit = [False] * (N + 1)
visit[V] = True
result = [V]
while q:
    node = q.pop(0)
    for i in graph[node]:
        if visit[i] == False:
            visit[i] = True
            q.append(i)
            result.append(i)
print(*result)
