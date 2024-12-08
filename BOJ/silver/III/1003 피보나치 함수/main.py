call_cnts = [[1, 0], [0, 1]]

for i in range(2, 41):
    call_cnts.append(
        [
            call_cnts[i - 2][0] + call_cnts[i - 1][0],
            call_cnts[i - 2][1] + call_cnts[i - 1][1],
        ]
    )

T = int(input())
for _ in range(T):
    n = int(input())
    print(*call_cnts[n])
