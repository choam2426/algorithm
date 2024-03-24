N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))


def find_max_value(board):
    max_value = 0
    for y in range(N):
        candy = None
        for x in range(N):
            if board[y][x] != candy:
                candy = board[y][x]
                count = 1
            else:
                count += 1
            if max_value < count:
                max_value = count
                if max_value == N:
                    return max_value

    for x in range(N):
        candy = None
        for y in range(N):
            if board[y][x] != candy:
                candy = board[y][x]
                count = 1
            else:
                count += 1
            if max_value < count:
                max_value = count
                if max_value == N:
                    return max_value
    return max_value


max_value = 0
for y in range(N):
    for x in range(N - 1):
        if board[y][x] == board[y][x + 1]:
            continue
        tmp = board[y][x]
        board[y][x] = board[y][x + 1]
        board[y][x + 1] = tmp
        value = find_max_value(board)
        board[y][x + 1] = board[y][x]
        board[y][x] = tmp
        if value > max_value:
            max_value = value
            if max_value == N:
                break
    if max_value == N:
        break

for x in range(N):
    for y in range(N - 1):
        if board[y][x] == board[y + 1][x]:
            continue
        tmp = board[y][x]
        board[y][x] = board[y + 1][x]
        board[y + 1][x] = tmp
        value = find_max_value(board)
        board[y + 1][x] = board[y][x]
        board[y][x] = tmp
        if value > max_value:
            max_value = value
            if max_value == N:
                break
    if max_value == N:
        break

print(max_value)
