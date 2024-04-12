test_case = int(input())

for _ in range(test_case):
    N, target = map(int, input().split())
    print_queue = list(map(int, input().split()))
    level_stack = sorted(print_queue)
    result = 0
    index = 0
    while print_queue[target]:
        if level_stack[-1] == print_queue[index]:
            print_queue[index] = False
            result += 1
            level_stack.pop()
        index += 1
        if index == len(print_queue):
            index = 0
    print(result)
