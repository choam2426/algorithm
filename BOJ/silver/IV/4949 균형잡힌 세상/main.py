while True:
    stack = []
    string = input()
    if string == ".":
        break
    for char in string:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif char == "[":
            stack.append("[")
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")
