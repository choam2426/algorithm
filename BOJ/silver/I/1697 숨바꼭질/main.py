x, goal = map(int, input().split())

distance = goal - x
time = 0
if distance <= 0:
    print(distance * -1)
else:
    while True:
        tmp = x
        x *= 2
        distance = goal - x
        if distance < 0:
            if (distance * -1) >= goal - tmp:
                time += goal - tmp
                break
            else:
                time += distance * -1
                break
        elif distance == 0:
            time += 1
            break
        time += 1
    print(time)
