N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()


def recursive(n, j, seq):
    if n == M:
        print(*seq)
        return

    for i in range(j, N):
        seq.append(numbers[i])
        recursive(n + 1, i, seq)
        seq.pop()


recursive(0, 0, [])
