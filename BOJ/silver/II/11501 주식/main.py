import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    result = 0
    max_price = 0
    for i in range(len(price) - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            result += max_price - price[i]
    print(result)
