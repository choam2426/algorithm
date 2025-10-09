n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 100001
st, en = 0, 0
tmp_sum = nums[st]
while True:
    if tmp_sum >= s:
        result = min(result, en - st + 1)
        tmp_sum -= nums[st]
        st += 1
    elif en < n - 1:
        en += 1
        tmp_sum += nums[en]
    else:
        tmp_sum -= nums[st]
        st += 1

    if st == n:
        break

print(result if result < 100001 else 0)
