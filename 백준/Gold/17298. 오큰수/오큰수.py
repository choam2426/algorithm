N = int(input())
numbers = list(map(int, input().split()))
stack = []
result = [-1] * N
for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        result[stack[-1]] = numbers[i]
        stack.pop()
    stack.append(i)

print(*result)
