N = int(input())

tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort()
room_end_times = [tasks.pop(0)[1]]
for task in tasks:
    for i, end_time in enumerate(room_end_times):
        if end_time > task[1]:
            room_end_times[i] = task[1]
        elif end_time <= task[0]:
            room_end_times[i] = task[1]
            break
    else:
        room_end_times.append(task[1])

print(len(room_end_times))
