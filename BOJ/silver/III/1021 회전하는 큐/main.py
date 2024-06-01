import copy
from collections import deque

N, M = map(int, input().split())
left_dq = deque(range(1, N + 1))
right_dq = copy.deepcopy(left_dq)
target_numbers = list(map(int, input().split()))
result = 0
for target_number in target_numbers:
    left_cnt = 0
    right_cnt = 0
    while True:
        if left_dq[0] == target_number:
            left_dq.popleft()
            right_dq = copy.deepcopy(left_dq)
            break
        elif right_dq[0] == target_number:
            right_dq.popleft()
            left_dq = copy.deepcopy(right_dq)
            break
        else:
            left_dq.rotate(-1)
            right_dq.rotate(1)
            result += 1
print(result)
