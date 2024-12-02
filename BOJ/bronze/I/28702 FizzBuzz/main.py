inputs = []
fizz_buzz = ["Fizz", "Buzz", "FizzBuzz"]
for _ in range(3):
    inputs.append(input())
for i, number in enumerate(inputs):
    if number in fizz_buzz:
        continue
    next_number = int(number) + 3 - i
result = ""
if next_number % 3 == 0:
    result += "Fizz"
if next_number % 5 == 0:
    result += "Buzz"
if result:
    print(result)
else:
    print(next_number)
