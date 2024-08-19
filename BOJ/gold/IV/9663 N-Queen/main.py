N = int(input())

straight_visit = [False] * N
diagonal_visit = [[False] * (2 * N - 1) for _ in range(2)]
result = 0


def back_tracking(depth):
    if depth == N:
        global result
        result += 1
        return

    for i in range(N):
        if straight_visit[i] or diagonal_visit[0][i + depth] or diagonal_visit[1][i - depth]:
            continue
        straight_visit[i] = True
        diagonal_visit[0][i + depth] = True
        diagonal_visit[1][i - depth] = True
        back_tracking(depth + 1)
        straight_visit[i] = False
        diagonal_visit[0][i + depth] = False
        diagonal_visit[1][i - depth] = False


back_tracking(0)
print(result)
