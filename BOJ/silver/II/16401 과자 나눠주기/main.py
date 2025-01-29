import sys

input = sys.stdin.readline
M, N = map(int, input().split())
pepero = list(map(int, input().split()))
pepero.sort()
start = 1
end = pepero[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in pepero:
        cnt += i // mid
    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
