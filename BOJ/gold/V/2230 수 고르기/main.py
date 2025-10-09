import sys

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
st, en = 0, 1
result = sys.maxsize
while True:
    if a[en] - a[st] >= m:
        result = min(result, a[en] - a[st])
        st += 1
    else:
        en += 1

    if en == n or st == n:
        break

print(result)
