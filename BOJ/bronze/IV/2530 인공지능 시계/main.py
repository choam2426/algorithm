h, m, s = map(int, input().split())
cooking_time = int(input())

total_second = (h * 3600) + (m * 60) + s + cooking_time
total_second %= 86400

print(total_second // 3600, total_second % 3600 // 60, total_second % 60)
