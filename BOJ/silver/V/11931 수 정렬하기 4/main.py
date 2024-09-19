import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = [False] * 2000001

for _ in range(N):
    num = int(input())
    arr[num] = True

for i in range(1000000, -1000001, -1):
    if arr[i]:
        print(i)
