N, M = map(int, input().split())


def recursive(n, seq):
    if n == M:
        print(*seq)
        return

    for j in range(1, N + 1):
        seq.append(j)
        recursive(n + 1, seq)
        seq.pop()


recursive(0, [])
