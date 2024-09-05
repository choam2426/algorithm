def back_tracking(seq, numbers, visit):
    if len(seq) == 6:
        print(*seq)
        return
    for i in range(len(numbers)):
        if visit[i] or seq[-1] > numbers[i]:
            continue
        seq.append(numbers[i])
        visit[i] = True
        back_tracking(seq, numbers, visit)
        seq.pop()
        visit[i] = False


def select_number(set_len, numbers):
    visit = [False] * set_len
    for i in range(set_len):
        seq = [numbers[i]]
        visit[i] = True
        back_tracking(seq, numbers, visit)


while True:
    S = list(map(int, input().split()))
    set_len = S.pop(0)
    if set_len == 0:
        break
    select_number(set_len, S)
    print()
