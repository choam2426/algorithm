from copy import deepcopy

N, M = map(int, input().split())


def recursive(sequence, unused_numbers):
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(len(unused_numbers)):
        now_sequence = deepcopy(sequence)
        now_unused_numbers = deepcopy(unused_numbers)
        number = now_unused_numbers.pop(i)
        now_sequence.append(number)
        recursive(now_sequence, now_unused_numbers)


recursive([], [i for i in range(1, N + 1)])
