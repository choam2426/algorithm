target_channel = int(input())
result = abs(target_channel - 100)
n = int(input())
if n == 0:
    if result > len(str(target_channel)):
        print(len(str(target_channel)))
    else:
        print(result)
else:
    buttons = list(map(str, input().split()))
    if target_channel == 100:
        print(0)
    elif n == 10:
        print(abs(target_channel - 100))
    else:
        plus_start_channel = target_channel
        minus_start_channel = target_channel
        while True:
            if minus_start_channel >= 0:
                for button in buttons:
                    if button in str(minus_start_channel):
                        break
                else:
                    tmp = len(str(minus_start_channel)) + (
                        target_channel - minus_start_channel
                    )
                    if result > tmp:
                        result = tmp
                    print(result)
                    break
            for button in buttons:
                if button in str(plus_start_channel):
                    break
            else:
                tmp = len(str(plus_start_channel)) + (
                    plus_start_channel - target_channel
                )
                if result > tmp:
                    result = tmp
                print(result)
                break
            plus_start_channel += 1
            minus_start_channel -= 1
