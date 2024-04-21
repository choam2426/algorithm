N = int(input())
height_list = [int(input()) for _ in range(N)]
stack = []
result = 0
for height in height_list:

    while stack:
        if stack[-1] <= height:
            stack.pop()
        else:
            result += len(stack)
            break
    stack.append(height)

print(result)
