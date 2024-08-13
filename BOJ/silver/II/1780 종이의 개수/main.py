N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]


def check_paper(paper: list) -> bool:
    n = len(paper)
    start_number = paper[0][0]
    if n == 1:
        result[start_number] += 1
        return True

    for y in range(n):
        for x in range(n):
            if paper[y][x] != start_number:
                return False
    result[start_number] += 1
    return True


def count_paper(paper: list) -> None:
    if check_paper(paper):
        return
    n = len(paper) // 3

    for i in range(3):
        for j in range(3):
            sliced_paper = [paper[(i * n) + k][j * n : (j + 1) * n] for k in range(n)]
            count_paper(sliced_paper)


count_paper(paper)
for i in range(-1, 2):
    print(result[i])
