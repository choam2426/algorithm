N = int(input())
scores = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N <= 2:
    print(sum(scores))
    exit()
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]
for i in range(3, N + 1):
    dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])
print(dp[-1])
