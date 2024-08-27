N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()


def recursive(seq):
    if len(seq) == M:
        print(*seq)
        return

    last_number = 0
    for i in range(N):
        if last_number == numbers[i]:
            continue
        last_number = numbers[i]
        seq.append(numbers[i])
        recursive(seq)
        seq.pop()


recursive([])
