while True:
    result = [0, 0, 0, 0]
    try:
        for char in input():
            ascii = ord(char)
            if ascii == 0x20:
                result[3] += 1
            elif ascii <= 0x39:
                result[2] += 1
            elif ascii <= 0x5A:
                result[1] += 1
            else:
                result[0] += 1
        for i in result:
            print(i, end=" ")
        print()
    except EOFError:
        break
