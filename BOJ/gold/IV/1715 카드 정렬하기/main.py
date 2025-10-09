# https://www.acmicpc.net/problem/1715
import heapq as hq

heap = []
n = int(input())
for _ in range(n):
    hq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    tmp = 0
    a = hq.heappop(heap)
    b = hq.heappop(heap)
    tmp += a + b
    result += tmp
    hq.heappush(heap, tmp)

print(result)
