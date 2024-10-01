numbers = []

while True:
    _input = input()

    numbers.extend(list(_input.split()))

    if (len(numbers) - 1) == int(numbers[0]):
        break
N = numbers.pop(0)
reverse_numbers = []
for number in numbers:
    reverse_numbers.append(int(number[::-1]))

reverse_numbers.sort()

print("\n".join(str(number) for number in reverse_numbers))
