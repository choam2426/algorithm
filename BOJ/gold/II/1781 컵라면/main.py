# https://www.acmicpc.net/problem/1781
import heapq as hq
import sys

input = sys.stdin.readline
problems = [tuple(map(int, input().split())) for _ in range(int(input()))]
problems.sort(key=lambda x: x[0])

result_heap = [problems[0][1]]

turn = 2
for deadline, reward in problems[1:]:
    if deadline >= turn:
        hq.heappush(result_heap, reward)
        turn += 1
    else:
        if reward > result_heap[0]:
            hq.heapreplace(result_heap, reward)
print(sum(result_heap))
