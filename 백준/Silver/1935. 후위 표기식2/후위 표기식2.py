N = int(input())
expression = input()
value = []
stack = []
for _ in range(N):
    value.append(int(input()))

for c in expression:
    if ord(c) > 64:
        stack.append(value[ord(c) - 65])
        continue
    if c == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif c == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif c == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif c == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)

result = stack.pop()
print(f"{result:.2f}")
