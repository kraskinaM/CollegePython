num1 = float(input())
num2 = float(input())
num3 = float(input())

choice = input("Введите sum или product: ").strip().lower()
if choice == 'sum':
    result = num1 + num2 + num3
    print(result)
elif choice == 'product':
    result = num1 * num2 * num3
    print(result)
