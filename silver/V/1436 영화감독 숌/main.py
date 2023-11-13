n = int(input())
number = 666
index = 1

while index != n:
    six_index = 0
    number += 1
    for i in str(number):
        if i == "6":
            six_index += 1
        else:
            six_index = 0
        if six_index == 3:
            index += 1
            break


print(number)
