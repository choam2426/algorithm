N = int(input())

board = [[" "] * N for _ in range(N)]


def paint_board(n: int, x: int, y: int) -> None:
    if n == 1:
        board[y][x] = "*"
    else:
        n = n // 3
        for i in range(3):
            for j in range(3):
                if i * j == 1:
                    continue
                paint_board(n, x + (j * n), y + (n * i))


paint_board(N, 0, 0)

for line in board:
    print("".join(line))
