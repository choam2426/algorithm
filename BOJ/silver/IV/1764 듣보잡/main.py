N, M = map(int, input().split())
names = [input() for _ in range(N + M)]
name_dict = {}
dbjs = []
for name in names:
    if name_dict.get(name, 0) == 0:
        name_dict[name] = 1
    else:
        dbjs.append(name)
dbjs.sort()
print(f"{len(dbjs)}\n" + "\n".join(dbjs))
