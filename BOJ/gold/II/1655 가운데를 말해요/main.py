# https://www.acmicpc.net/problem/1655

import heapq as hq
import sys

input = sys.stdin.readline
n = int(input())
max_heap = [-int(input())]
min_heap = []
print(-max_heap[0])
for _ in range(n - 1):
    number = int(input())
    if number < -max_heap[0]:
        hq.heappush(max_heap, -number)
    else:
        hq.heappush(min_heap, number)

    if (len(max_heap) - len(min_heap)) == 2:
        hq.heappush(min_heap, -hq.heappop(max_heap))
    elif (len(max_heap) - len(min_heap)) == -1:
        hq.heappush(max_heap, -hq.heappop(min_heap))
    print(-max_heap[0])
