n = int(input())
x = list(map(int, input().split()))
x_sorted = sorted(set(x))  # x에서 중복값을 제거하고 정렬
comp = {}  # 압축된 값을 저장할 dictionary
for index, number in enumerate(x_sorted):  # 각 숫자의 index를 comp에 저장
    comp[number] = index

for i in x:
    print(comp[i], end=" ")  # 좌표를 압축해서 출력
