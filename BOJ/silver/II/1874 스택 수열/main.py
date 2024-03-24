N = int(input())
sequences = [int(input()) for _ in range(N)]
number = 1
sequence_index = 0
stack = []
result = []
while sequence_index < len(sequences):
    if len(stack) == 0:
        result.append("+")
        stack.append(number)
        number += 1

    if sequences[sequence_index] == stack[-1]:
        result.append("-")
        stack.pop()
        sequence_index += 1
    elif sequences[sequence_index] < stack[-1]:
        print("NO")
        break
    else:
        result.append("+")
        stack.append(number)
        number += 1

if sequence_index == len(sequences):
    for execute in result:
        print(execute)
