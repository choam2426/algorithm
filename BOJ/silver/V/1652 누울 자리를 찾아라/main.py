N = int(input())
room = [input() for _ in range(N)]
w, h = 0, 0
for i in range(N):
    w_cnt = 0
    h_cnt = 0
    for j in range(N):
        if room[i][j] != "X":
            w_cnt += 1
            if w_cnt == 2:
                w += 1
        else:
            w_cnt = 0

        if room[j][i] != "X":
            h_cnt += 1
            if h_cnt == 2:
                h += 1
        else:
            h_cnt = 0

print(w, h)
