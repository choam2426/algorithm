M, N = map(int, input().split())
order_map = {}
for _ in range(M):
    planets = list(map(int, input().split()))
    sorted_planets = sorted(planets)
    order = {sorted_planets[i]: i for i in range(len(sorted_planets))}
    order = tuple([order[planet] for planet in planets])
    order_map[order] = order_map.get(order, 0) + 1
result = sum(order * (order - 1) // 2 for order in order_map.values())
print(result)
