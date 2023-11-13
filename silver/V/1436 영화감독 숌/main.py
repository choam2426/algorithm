n = int(input())
number = 666
index = 1  # 6이 3번 연속된 숫자가 몇번 있었는지 기록

while index != n:  # index가 n에 도달하면 종료
    six_index = 0  # 6이 몇번 반복된지 기록
    number += 1
    for i in str(number):
        if i == "6":  # 6일 경우 six_index 값 증가
            six_index += 1
        else:  # 6이 아닐 경우 연속이 아니므로 초기화
            six_index = 0
        if six_index == 3:  # 6이 3번 연속 나오면 escape
            index += 1
            break

print(number)
