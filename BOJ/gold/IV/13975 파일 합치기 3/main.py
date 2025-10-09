# https://www.acmicpc.net/problem/13975
import heapq as hq
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    input()
    pages = list(map(int, input().split()))
    hq.heapify(pages)
    result = 0
    while len(pages) > 1:
        tmp = hq.heappop(pages) + hq.heappop(pages)
        result += tmp
        hq.heappush(pages, tmp)
    print(result)
