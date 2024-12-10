from collections import deque

N = int(input())
pair = int(input())
connections = [[] for _ in range(N + 1)]
is_infected = [False] * (N + 1)
for _ in range(pair):
    node1, node2 = map(int, input().split())
    connections[node1].append(node2)
    connections[node2].append(node1)
is_infected[1] = True
dq = deque([1])
while dq:
    i = dq.popleft()
    for t in connections[i]:
        if not is_infected[t]:
            is_infected[t] = True
            dq.append(t)
print(is_infected.count(True) - 1)
