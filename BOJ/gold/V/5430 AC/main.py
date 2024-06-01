from collections import deque

T = int(input())
for _ in range(T):
    commands = input()
    commands = commands.replace("RR", "")
    n = int(input())
    arr = input()
    vector = 1
    if len(arr) < 3:
        dq = deque()
    else:
        dq = deque(arr[1:-1].split(","))

    for command in commands:
        if command == "R":
            vector *= -1
        else:
            if len(dq) == 0:
                print("error")
                break
            if vector == 1:
                dq.popleft()
            else:
                dq.pop()
    else:
        if vector == 1:
            result = "[" + ",".join(dq) + "]"
        else:
            dq.reverse()
            result = "[" + ",".join(dq) + "]"
        print(result)
