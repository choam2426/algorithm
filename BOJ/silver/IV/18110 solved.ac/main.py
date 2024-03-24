import sys
from math import floor

input = sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(n)]
    scores.sort()
    cut = floor((n * 0.15) + 0.5)
    if cut:
        result = floor(sum(scores[cut:-cut]) / (n - cut * 2) + 0.5)
        print(result)
    else:
        result = floor(sum(scores) / n + 0.5)
        print(result)
