from collections import deque


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs():
    n = int(input())
    start = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    end = tuple(map(int, input().split()))
    visited = [False] * (n)
    dq = deque([start])
    while dq:
        x, y = dq.popleft()
        if get_distance((x, y), end) <= 1000:
            return "happy"
        for i, store in enumerate(stores):
            if not visited[i] and get_distance((x, y), store) <= 1000:
                dq.append(store)
                visited[i] = True
    else:
        return "sad"


t = int(input())
for _ in range(t):
    print(bfs())
