stack = []
result = 0
tmp = 0
wrong_flag = False
for char in input():
    if char == ")":
        while stack:
            if stack[-1] == "(":
                if tmp:
                    tmp *= 2
                else:
                    tmp = 2
                stack.pop()
                break
            elif stack[-1] == "[":
                wrong_flag = True
                break
            else:
                tmp += stack.pop()
        stack.append(tmp)
        tmp = 0
    elif char == "]":
        while stack:
            if stack[-1] == "[":
                if tmp:
                    tmp *= 3
                else:
                    tmp = 3
                stack.pop()
                break
            elif stack[-1] == "(":
                wrong_flag = True
                break
            else:
                tmp += stack.pop()
        stack.append(tmp)
        tmp = 0
    else:
        stack.append(char)
    if wrong_flag:
        print(0)
        break
else:
    print(sum(stack))
