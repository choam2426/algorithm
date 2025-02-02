import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    cut = 0
    for tree in trees:
        if tree > mid:
            cut += tree - mid
    if cut >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
