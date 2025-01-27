# 이분 탐색으로 푼 풀이
from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
for target in map(int, input().split()):
    print(1 if bisect_left(cards, target) != bisect_right(cards, target) else 0, end=" ")

# 해시맵(dict)로 푼 풀이
N = int(input())
cards = list(map(int, input().split()))
card_map = {card: 1 for card in cards}
M = int(input())
for target in map(int, input().split()):
    print(card_map.get(target, 0), end=" ")
