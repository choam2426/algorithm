N = int(input())
pack_price = [0]
pack_price.extend(list(map(int, input().split())))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = pack_price[i]
    for j in range(1, i):
        dp[i] = min(dp[i], pack_price[j] + dp[i - j])

print(dp[-1])
