T = int(input())
seq = [1, 1, 1]
for i in range(3, 100):
    seq.append(seq[i - 2] + seq[i - 3])

for _ in range(T):
    print(seq[int(input()) - 1])
