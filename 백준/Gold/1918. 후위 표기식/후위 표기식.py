expression = input()
stack = []


def is_top():
    if stack and stack[-1] != "(":
        return True
    return False


def is_top_2():
    if stack and stack[-1] != "(":
        if stack[-1] == "+" or stack[-1] == "-":
            return False
        return True
    return False


for c in expression:
    if ord(c) > 64:
        print(c, end="")
        continue

    if c == "+":
        while is_top():
            print(stack.pop(), end="")
    elif c == "-":
        while is_top():
            print(stack.pop(), end="")
    elif c == "*":
        while is_top_2():
            print(stack.pop(), end="")
    elif c == "/":
        while is_top_2():
            print(stack.pop(), end="")
    elif c == ")":
        while stack and stack[-1] != "(":
            print(stack.pop(), end="")
        stack.pop()
        continue
    stack.append(c)
else:
    while stack:
        print(stack.pop(), end="")
