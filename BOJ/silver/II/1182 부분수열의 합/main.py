N, S = map(int, input().split())

numbers = list(map(int, input().split()))
visit = [False] * N


def back_tracking(n, index):
    result = 0
    if n == S and True in visit:
        result += 1

    for i in range(index, N):
        if visit[i]:
            continue
        n += numbers[i]
        visit[i] = True
        result += back_tracking(n, i)
        n -= numbers[i]
        visit[i] = False
    return result


print(back_tracking(0, 0))
