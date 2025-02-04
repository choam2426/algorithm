N = int(input())
arr = list(map(int, input().split()))
left, right = 0, N - 1
result = (arr[left] + arr[right], left, right)
while True:
    if left == right:
        break
    tmp = arr[left] + arr[right]
    if abs(tmp) < abs(result[0]):
        result = (tmp, left, right)
    if tmp < 0:
        left += 1
    elif tmp > 0:
        right -= 1
    else:
        result = (0, left, right)
        break


print(arr[result[1]], arr[result[2]])
