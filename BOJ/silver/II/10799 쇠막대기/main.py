result = 0
stack = []
tmp = ""
for char in input():
    if char == "(":
        stack.append(1)
    elif char == ")":
        stack.pop()
        if tmp == "(":
            result += len(stack)
        else:
            result += 1
    tmp = char

print(result)
