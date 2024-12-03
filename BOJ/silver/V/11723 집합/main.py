import sys

input = sys.stdin.readline
s = [False] * 21
M = int(input())

for _ in range(M):
    command = input().split()
    if command[0] == "add":
        s[int(command[1])] = True
    elif command[0] == "remove":
        s[int(command[1])] = False
    elif command[0] == "check":
        print(1 if s[int(command[1])] else 0)
    elif command[0] == "toggle":
        s[int(command[1])] = not s[int(command[1])]
    elif command[0] == "all":
        s = [True] * 21
    else:
        s = [False] * 21
