import sys

input = sys.stdin.readline
N, M = map(int, input().split())
site_map = {}
for _ in range(N):
    domain, password = map(str, input().split())
    site_map[domain] = password

for _ in range(M):
    domain = input().strip()
    print(site_map[domain])
