T = int(input())

for _ in range(T):
    N = int(input())
    surve = list(map(int, input().split()))
    visited = [False] * N
    student_count = 0
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        team_member = [i]
        next = surve[i] - 1
        while True:
            if visited[next]:
                if next in team_member:
                    start = team_member.index(next)
                    student_count += len(team_member) - start
                break
            team_member.append(next)
            visited[next] = True
            next = surve[next] - 1

    print(N - student_count)
