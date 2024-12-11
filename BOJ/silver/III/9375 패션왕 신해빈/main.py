T = int(input())

for _ in range(T):
    closet = {}
    n = int(input())
    for _ in range(n):
        name, clothes_type = map(str, input().split())
        if clothes := closet.get(clothes_type):
            clothes.append(name)
            closet[clothes_type] = clothes
        else:
            closet[clothes_type] = [name]

    result = 1
    for clothes_type, clothes in closet.items():
        result *= len(clothes) + 1
    print(result - 1)
