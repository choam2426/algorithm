S = list(input())
suffix_list = []

for i in range(len(S)):
    suffix = "".join(S[i:])
    suffix_list.append(suffix)
suffix_list.sort()
for suffix in suffix_list:
    print(suffix)
