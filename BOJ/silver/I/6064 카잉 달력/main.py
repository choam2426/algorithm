def find_year(m, n, x, y):
    a, b = 1, 1
    year = 1
    while a != x or b != y:
        a += 1
        b += 1
        year += 1
        if a > m:
            a -= m
        if b > n:
            b -= n
    return year


n = int(input())

for _ in range(n):
    M, N, X, Y = map(int(input().split()))
    print()
