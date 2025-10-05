# https://www.acmicpc.net/problem/11055
from copy import deepcopy

n = int(input())
arr = list(map(int, input().split()))
d = deepcopy(arr)
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + arr[i])
print(max(d))
