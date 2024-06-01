import sys

queue = [0] * 2000001
head = 0
tail = 0
N = int(input())
for _ in range(N):
    cmd = list(sys.stdin.readline().strip().split())

    if cmd[0] == "push":
        queue[tail] = cmd[1]
        tail += 1
    elif cmd[0] == "pop":
        if head >= tail:
            print(-1)
        else:
            print(queue[head])
            head += 1
    elif cmd[0] == "size":
        print(tail - head)
    elif cmd[0] == "empty":
        if head == tail:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if head == tail:
            print(-1)
        else:
            print(queue[head])
    elif cmd[0] == "back":
        if head == tail:
            print(-1)
        else:
            print(queue[tail - 1])
