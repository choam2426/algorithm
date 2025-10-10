# https://www.acmicpc.net/problem/14425
n, m = map(int, input().split())

str_map = {input(): 1 for _ in range(n)}

result = 0
for _ in range(m):
    s = input()
    if str_map.get(s):
        result += 1
print(result)
