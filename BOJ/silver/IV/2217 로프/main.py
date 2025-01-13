N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort()
max_weight = 0
number_of_ropes = len(ropes)
for i in range(number_of_ropes):
    tmp_max_weight = ropes[i] * (number_of_ropes - i)
    if max_weight < tmp_max_weight:
        max_weight = tmp_max_weight
print(max_weight)
