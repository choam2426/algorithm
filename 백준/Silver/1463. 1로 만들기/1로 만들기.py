N = int(input())

dp_list = [0] * (N + 1)

for i in range(2, N + 1):
    dp_list[i] = dp_list[i - 1] + 1

    if i % 2 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i // 2] + 1)
    if i % 3 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i // 3] + 1)

print(dp_list[N])
