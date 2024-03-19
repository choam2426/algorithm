string = input()

for char in string:
    if char.isalpha():
        if char.isupper():
            rot13 = ord(char) + 13
            if rot13 > 90:
                rot13 -= 26
            print(chr(rot13), end="")
        elif char.islower():
            rot13 = ord(char) + 13
            if rot13 > 122:
                rot13 -= 26
            print(chr(rot13), end="")
    else:
        print(char, end="")
