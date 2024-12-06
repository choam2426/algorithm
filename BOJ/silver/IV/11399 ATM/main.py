N = int(input())
times = list(map(int, input().split()))
times.sort()
result = 0
for i, time in enumerate(times):
    result += time * (N - i)
print(result)
