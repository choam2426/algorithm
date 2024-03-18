import sys

input = sys.stdin.readline

max = 1000000

gN_list = [1] * (max + 1)

for i in range(2, max + 1):
    j = 1
    while True:
        if i * j < max + 1:
            gN_list[i * j] += i
            j += 1
        else:
            break
    gN_list[i] += gN_list[i - 1]


T = int(input())
for _ in range(T):
    N = int(input())
    print(gN_list[N])
