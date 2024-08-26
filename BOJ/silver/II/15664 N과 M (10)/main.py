N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
visit = [False] * N


def recursive(index, seq):
    if len(seq) == M:
        print(*seq)
        return

    last_number = 0
    for i in range(index, N):
        if visit[i] or last_number == numbers[i]:
            continue
        last_number = numbers[i]
        seq.append(numbers[i])
        visit[i] = True
        recursive(i + 1, seq)
        seq.pop()
        visit[i] = False


recursive(0, [])
