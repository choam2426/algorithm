import sys

input = sys.stdin.readline
N, M = map(int, input().split())

arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
result = []
index_1 = 0
index_2 = 0

while True:
    if index_1 == N:
        result.extend(arr2[index_2:])
        break
    elif index_2 == M:
        result.extend(arr1[index_1:])
        break
    if arr1[index_1] > arr2[index_2]:
        result.append(arr2[index_2])
        index_2 += 1
    elif arr1[index_1] < arr2[index_2]:
        result.append(arr1[index_1])
        index_1 += 1
    else:
        result.append(arr1[index_1])
        result.append(arr2[index_2])
        index_1 += 1
        index_2 += 1
print(*result)
