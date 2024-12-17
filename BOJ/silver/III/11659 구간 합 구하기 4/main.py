import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sums = [0]

for number in numbers:
    sums.append(sums[-1] + number)

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i - 1])
