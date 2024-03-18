esm = list(map(int, input().split()))
year = 1
tmp = [1, 1, 1]
ems_range = [15, 28, 19]
while True:
    for i in range(3):
        if esm[i] == tmp[i]:
            continue
        else:
            break
    else:
        print(year)
        break

    year += 1

    for i in range(3):
        tmp[i] += 1
        if tmp[i] > ems_range[i]:
            tmp[i] -= ems_range[i]
