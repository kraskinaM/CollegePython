count = 0
for n in range(100,1000):
    a = n // 100
    b = (n // 10) %10
    c = n % 10

    if (a == b or a == c or b == c) and not (a == b == c):
        count += 1

print(count)