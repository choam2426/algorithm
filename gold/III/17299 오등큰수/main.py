N = int(input())
numbers = list(map(int, input().split()))
f = [0] * 1000001
result = [-1] * N
stack = []

for number in numbers:
    f[number] += 1

for i in range(N):
    while stack and f[numbers[stack[-1]]] < f[numbers[i]]:
        result[stack[-1]] = numbers[i]
        stack.pop()
    stack.append(i)
print(*result)
