N, M = map(int, input().split())
cards = list(map(int, input().split()))
for _ in range(M):
    min1 = cards.pop(cards.index(min(cards)))
    min2 = cards.pop(cards.index(min(cards)))
    for _ in range(2):
        cards.append(min1 + min2)
print(sum(cards))
