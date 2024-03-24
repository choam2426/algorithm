import math
import sys

input = sys.stdin.readline


def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


max = 1000000

prime_numbers = [True] * 1000001
for i in range(3, 1000, 2):
    if prime_numbers[i]:
        for j in range(3, max // i + 1, 2):
            prime_numbers[i * j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for a in range(3, n // 2 + 1, 2):
        if not prime_numbers[a]:
            continue
        b = n - a
        if not prime_numbers[b]:
            continue
        else:
            print(f"{n} = {a} + {b}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
