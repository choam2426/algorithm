import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
result = []
for c in string:
    try:
        i = bomb.index(c)
        if stack and i == stack[-1] + 1 or i == 0:
            stack.append(i)
            if stack[-1] == len(bomb) - 1:
                for _ in range(len(bomb)):
                    stack.pop()
        else:
            for j in stack:
                result.append(bomb[j])
            result.append(c)

    except ValueError:
        for j in stack:
            result.append(bomb[j])
        result.append(c)
else:
    for j in stack:
        result.append(bomb[j])
if result:
    print("".join(result))
else:
    print("FRULA")
