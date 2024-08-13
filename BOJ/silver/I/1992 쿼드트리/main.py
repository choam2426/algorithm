N = int(input())

pixel = [list(input()) for _ in range(N)]

result = []


def check_pixel(pixel: list) -> bool:
    n = len(pixel)
    start_number = pixel[0][0]
    if n == 1:
        result.append(start_number)
        return True

    for y in range(n):
        for x in range(n):
            if pixel[y][x] != start_number:
                return False
    result.append(start_number)
    return True


def div_pixel(pixel: list) -> None:
    if check_pixel(pixel):
        return
    n = len(pixel) // 2
    result.append("(")
    for i in range(2):
        for j in range(2):
            sliced_pixel = [pixel[(i * n) + k][j * n : (j + 1) * n] for k in range(n)]
            div_pixel(sliced_pixel)
    result.append(")")


div_pixel(pixel)
print("".join(result))
