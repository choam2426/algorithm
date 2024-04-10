from bisect import bisect_left, bisect_right

N = int(input())
array1 = list(map(int, input().split()))
array1.sort()
M = int(input())
array2 = list(map(int, input().split()))

for number in array2:
    print(bisect_right(array1, number) - bisect_left(array1, number), end=" ")
