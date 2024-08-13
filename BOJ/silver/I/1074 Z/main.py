N, R, C = map(int, input().split())


def recursive(r, c, n, v):
    if n == 2:
        result = v + (r * 2) + c
        print(result)
        exit(0)
    n = n // 2

    if r < n and c < n:
        recursive(r, c, n, v)

    elif r < n and c >= n:
        recursive(r, c - n, n, v + (n**2))

    elif r >= n and c < n:
        recursive(r - n, c, n, v + (n**2) * 2)

    elif r >= n and c >= n:
        recursive(r - n, c - n, n, v + (n**2) * 3)


recursive(R, C, 2**N, 0)
