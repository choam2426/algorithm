N = int(input())

for _ in range(N):
    sentence = input().split()
    for word in sentence:
        word_list = list(word)
        for _ in range(len(word_list)):
            print(word_list.pop(), end="")
        else:
            print(" ", end="")
    else:
        print()
