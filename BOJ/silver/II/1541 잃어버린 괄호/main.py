s = input()
chunks = list(s.split("-"))
numbers = []
for chunk in chunks:
    tmp = [int(i) for i in chunk.split("+")]
    numbers.append(sum(tmp))

print(numbers[0] - sum(numbers[1:]))
