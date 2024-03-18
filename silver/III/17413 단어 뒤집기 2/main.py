string = input()
stack = []
tag_flag = False
result = ""
for char in string:
    if char == "<":
        tag_flag = True
    elif char == ">":
        result += char
        tag_flag = False
        continue

    if tag_flag:
        while stack:
            result += stack.pop()
        result += char
    elif char == " ":
        while stack:
            result += stack.pop()
        result += char
    else:
        stack.append(char)
while stack:
    result += stack.pop()
print(result)
