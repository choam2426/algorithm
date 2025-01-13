N = int(input())

tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort()
result = 1
tmp_end_time = tasks.pop(0)[1]
for task in tasks:
    if tmp_end_time > task[1]:
        tmp_end_time = task[1]
    elif tmp_end_time <= task[0]:
        result += 1
        tmp_end_time = task[1]
print(result)
