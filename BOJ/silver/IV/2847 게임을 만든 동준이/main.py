N = int(input())
scores = [int(input()) for _ in range(N - 1)]
recent_score = int(input())
result = 0
while scores:
    score = scores.pop()
    if score >= recent_score:
        result += score - recent_score + 1
        score = recent_score - 1
    recent_score = score
print(result)
