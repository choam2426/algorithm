import sys

stack = []
result = 0
N = int(sys.stdin.readline().strip())

for _ in range(N):
    height = int(sys.stdin.readline().strip())
    while stack and stack[-1][0] < height:
        result += stack.pop()[1]

    if stack and stack[-1][0] == height:
        result += stack[-1][1]
        stack.append((height, stack.pop()[1] + 1))
        if len(stack) > 1:
            result += 1
    else:
        if stack:
            result += 1
        stack.append((height, 1))


print(result)
