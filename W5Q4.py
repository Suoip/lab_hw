logs = []
count = {}
for log in logs:
    if log in count:
        count[log] += 1
    else:
        count[log] = 1

print(count)