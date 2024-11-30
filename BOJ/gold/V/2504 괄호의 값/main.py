from collections import deque
import sys

stack = deque()
string = input()
result = 0
tmp = 1
for i, c in enumerate(string):
    if c == "(":
        tmp *= 2
        stack.append((c, i))
    elif c == "[":
        tmp *= 3
        stack.append((c, i))
    else:
        if not stack:
            print(0)
            sys.exit(0)
        t_c, t_i = stack.pop()
        if c == ")" and t_c == "(":
            tmp //= 2
            if i - t_i == 1:
                result += 2 * tmp
        elif c == "]" and t_c == "[":
            tmp //= 3
            if i - t_i == 1:
                result += 3 * tmp
        else:
            print(0)
            sys.exit(0)

if stack:
    print(0)
else:
    print(result)
