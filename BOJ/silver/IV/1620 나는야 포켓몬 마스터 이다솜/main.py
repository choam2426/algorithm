import sys

input = sys.stdin.readline
N, M = map(int, input().split())
pokemon_dict1 = {}
pokemon_dict2 = {}
for i in range(N):
    pokemon_name = input().strip()
    pokemon_dict1[pokemon_name] = i + 1
    pokemon_dict2[i + 1] = pokemon_name

for _ in range(M):
    q = input().strip()
    if ord(q[0]) > 64:
        print(pokemon_dict1[q])
    else:
        print(pokemon_dict2[int(q)])
