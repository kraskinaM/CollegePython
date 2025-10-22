n =input(" Введите число:")
result = ""
for c in n:
    if c != "3" and c != "6":
        result += c

if not result:
    result = "0"

print(result)