expr = input("Введите выражение:")
if "+" in expr:
    a, b = expr.split("+")
    result = float(a) + float(b)
    print(result)
elif "-" in expr:
    a, b = expr.split("-")
    result = float(a) - float(b)
    print(result)
elif "*" in expr:
    a, b = expr.split("*")
    result = float(a) * float(b)
    print(result)
else:
    a, b = expr.split("/")
    result = float(a) / float(b)
    print(result)