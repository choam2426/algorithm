import sys

main_stack = list(input())
tmp_stack = []
n = int(input())

for _ in range(n):

    command = list(sys.stdin.readline().split())
    if command[0] == "L":
        if len(main_stack):
            tmp_stack.append(main_stack.pop())
        else:
            continue
    elif command[0] == "D":
        if len(tmp_stack):
            main_stack.append(tmp_stack.pop())
        else:
            continue
    elif command[0] == "B":
        if len(main_stack) < 1:
            continue
        else:
            main_stack.pop()
    else:
        main_stack.append(command[1])

else:
    for _ in range(len(tmp_stack)):
        main_stack.append(tmp_stack.pop())

for char in main_stack:
    print(char, end="")
