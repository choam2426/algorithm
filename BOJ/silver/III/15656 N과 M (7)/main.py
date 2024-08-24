N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()


def recursive(n, seq):
    if n == M:
        print(*seq)
        return

    for i in range(N):
        seq.append(numbers[i])
        recursive(n + 1, seq)
        seq.pop()


recursive(0, [])
