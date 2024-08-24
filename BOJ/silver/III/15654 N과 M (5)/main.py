N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
visit = [False] * N


def recursive(n, seq):
    if n == M:
        print(*seq)
        return

    for i in range(N):
        if visit[i]:
            continue
        seq.append(numbers[i])
        visit[i] = True
        recursive(n + 1, seq)
        seq.pop()
        visit[i] = False


recursive(0, [])
