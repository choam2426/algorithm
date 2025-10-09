# https://www.acmicpc.net/problem/1927
import heapq as hq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for cmd in [int(input()) for _ in range(n)]:
    if cmd == 0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, cmd)
