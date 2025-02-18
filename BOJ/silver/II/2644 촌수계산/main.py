from collections import deque

N = int(input())
start, end = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N + 1)
dq = deque([(start, 0)])
visited[start] = True
while dq:
    node, depth = dq.popleft()
    if node == end:
        print(depth)
        break
    for d_node in graph[node]:
        if not visited[d_node]:
            dq.append((d_node, depth + 1))
            visited[node] = True
else:
    print(-1)
