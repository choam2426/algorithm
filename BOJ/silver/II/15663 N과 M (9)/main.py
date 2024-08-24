N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
visit = [False] * N


def recursive(seq):
    if len(seq) == M:
        print(*seq)
        return

    last_number = 0
    for index, number in enumerate(numbers):
        if visit[index] or last_number == number:
            continue
        last_number = number
        seq.append(number)
        visit[index] = True
        recursive(seq)
        seq.pop()
        visit[index] = False


recursive([])
