# https://www.acmicpc.net/problem/1018
board = []
result = 64


def rewrite(x, y) -> int:
    case1 = 0  # 시작이 b
    case2 = 0  # 시작이 w

    for i in range(8):
        for j in range(8):
            color = board[y + i][x + j]
            if (i + j) % 2 == 0:
                if color == "B":
                    case2 += 1
                else:
                    case1 += 1
            else:
                if color == "B":
                    case1 += 1
                else:
                    case2 += 1

    return min(case1, case2)


N, M = map(int, input().split())
for _ in range(N):
    board.append(list(input()))
max_y = N - 7
max_x = M - 7

for y in range(max_y):
    for x in range(max_x):
        rewrite_count = rewrite(x=x, y=y)
        if rewrite_count < result:
            result = rewrite_count
        if result == 0:
            break

print(result)
