s = input()

result = [0, 0]

tmp_c = s[0]
for c in s[1:] + "2":
    if tmp_c == c:
        tmp_c = c
        continue

    if tmp_c == "1":
        result[0] += 1
    else:
        result[1] += 1
    tmp_c = c
print(min(result))
