# https://www.acmicpc.net/problem/11729
move_logs = []

def hanoi_tower(n: int, current_pole, target_pole, other_pole):
    if n == 1:
        move_logs.append((current_pole, target_pole))
    else:
        hanoi_tower(n - 1, current_pole, other_pole, target_pole)
        move_logs.append((current_pole, target_pole))
        hanoi_tower(n - 1, other_pole, target_pole, current_pole)

N = int(input())

hanoi_tower(N, 1, 3, 2)

print(len(move_logs))
for move_log in move_logs:
    print(*move_log)
