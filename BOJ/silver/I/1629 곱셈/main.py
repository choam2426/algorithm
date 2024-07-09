(
    a,
    b,
    c,
) = map(int, input().split())


def mul(a, b):
    if b == 1:
        return a % c
    value = mul(a, b // 2)
    result = value * value
    if b % 2 == 0:
        return result % c
    else:
        return (result * a) % c


print(mul(a, b))
