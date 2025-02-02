import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
numbers = [int(input()) for _ in range(int(input()))]
numbers.sort()
double_combinations = []
for i in range(len(numbers)):
    double_combinations.extend(numbers[i] + numbers[j] for j in range(i, len(numbers)))
double_combinations.sort()

for t in numbers[::-1]:
    for i in range(len(numbers)):
        if bisect_left(double_combinations, t - numbers[i]) < bisect_right(
            double_combinations, t - numbers[i]
        ):
            print(t)
            exit()
