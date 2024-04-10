N = int(input())
people = []
score = [1] * N
for _ in range(N):
    people.append(list(map(int, input().split())))

for i in range(N):
    current_person = people[i]
    for j in range(i + 1, N):
        next_person = people[j]
        if current_person[0] > next_person[0] and current_person[1] > next_person[1]:
            score[j] += 1
        elif current_person[0] < next_person[0] and current_person[1] < next_person[1]:
            score[i] += 1

print(*score)
