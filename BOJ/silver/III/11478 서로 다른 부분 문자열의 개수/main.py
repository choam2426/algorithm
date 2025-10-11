s = input()
n = len(s)
part = set()
for i in range(n):
    for j in range(n - i):
        part.add(s[j : j + i + 1])
print(len(part))
