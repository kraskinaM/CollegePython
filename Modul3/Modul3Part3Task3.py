count = 0
for n in range(100, 10000):
    s = str(n)
    if len(set(s)) == len(s):
        count += 1
print(count)