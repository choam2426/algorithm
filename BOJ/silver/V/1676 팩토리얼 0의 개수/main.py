N = int(input())
factorial = 1
for i in range(2, N + 1):
    factorial *= i

number_string = list(str(factorial))
count = 0
for num in number_string[::-1]:
    if num == "0":
        count += 1
    else:
        break
print(count)
