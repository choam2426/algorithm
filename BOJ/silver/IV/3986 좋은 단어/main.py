N = int(input())
result = 0

for _ in range(N):
    stack = []
    for char in input():
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        continue
    else:
        result += 1
print(result)
