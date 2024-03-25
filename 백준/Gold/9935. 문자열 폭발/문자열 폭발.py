import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
bomb_len = len(bomb)
stack = []
for c in string:
    stack.append(c)
    if len(stack) >= bomb_len and "".join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")
