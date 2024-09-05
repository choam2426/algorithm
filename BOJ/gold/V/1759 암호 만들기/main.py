L, C = map(int, input().split())

chars = sorted(list(input().split()))
visit = [False] * C
password = []


def check_vowel():
    result = 0
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        result += password.count(vowel)
    return result


def back_tracking(last_index):
    if len(password) == L:
        vowel_cnt = check_vowel()
        consonant_cnt = L - vowel_cnt
        if vowel_cnt > 0 and consonant_cnt > 1:
            print("".join(password))

    for i in range(C):
        if visit[i] or last_index > i:
            continue

        visit[i] = True
        password.append(chars[i])
        back_tracking(i)
        visit[i] = False
        password.pop()


back_tracking(0)
