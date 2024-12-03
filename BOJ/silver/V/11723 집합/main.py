import sys

input = sys.stdin.readline
s = 0
M = int(input())

for _ in range(M):
    command = input().strip().split()
    if command[0] == "add":
        s |= 1 << int(command[1])
    elif command[0] == "remove":
        s &= ~(1 << int(command[1]))
    elif command[0] == "check":
        print(1 if s & (1 << int(command[1])) else 0)
    elif command[0] == "toggle":
        s ^= 1 << int(command[1])
    elif command[0] == "all":
        s = (1 << 21) - 1
    elif command[0] == "empty":
        s = 0
