N = int(input())
size_cnt = list(map(int, input().split()))
T, P = map(int, input().split())

result = 0
for i in size_cnt:
    result += i // T + 1 if i % T else i // T
print(result)
print(N // P, N % P)
