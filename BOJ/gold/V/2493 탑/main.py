n = int(input())
tower = list(map(int, input().split()))
stack = []
result = [0] * n
for i in range(n - 1, -1, -1):
    while stack:
        if tower[i] > tower[stack[-1]]:
            result[stack[-1]] = i + 1
            stack.pop()
        else:
            break
    stack.append(i)
print(*result)
