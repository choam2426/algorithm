N, K = map(int, input().split())
K -= 1
queue = [i for i in range(1, N + 1)]
seq = []
index = 0
while queue:
    index += K
    index = index % len(queue)
    seq.append(queue.pop(index))
print("<" + str(seq)[1:-1] + ">")
