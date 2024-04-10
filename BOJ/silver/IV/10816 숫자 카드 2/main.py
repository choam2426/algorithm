numbers = [0] * 20000001

N = int(input())
for number in list(map(int, input().split())):
    number += 10000000
    numbers[number] += 1
M = int(input())
for number in list(map(int, input().split())):
    print(numbers[number + 10000000], end=" ")
