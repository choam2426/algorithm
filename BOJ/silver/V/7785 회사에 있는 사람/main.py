n = int(input())
log = {}
for _ in range(n):
    name, log_type = input().split()
    if log_type == "enter":
        log.update({name: 1})
    else:
        log.pop(name)

result = sorted(list(log.keys()), reverse=True)
print("\n".join(result))
