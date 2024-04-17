cables = []
K, N = map(int, input().split())
for _ in range(K):
    cables.append(int(input()))

max_value = max(cables)
min_value = 1
while max_value >= min_value:
    cutting_cables = 0
    tmp_value = (max_value + min_value) // 2
    for cable in cables:
        cutting_cables += cable // tmp_value

    if cutting_cables < N:
        max_value = tmp_value - 1
    elif cutting_cables >= N:
        min_value = tmp_value + 1

print(max_value)
