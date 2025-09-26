a = float(input())
b = float(input())
c = float(input())

print("Выберите операцию:")
print("1 - Найти максимум ")
print("2 - Найти минимум")
print("3 - Найти среднее арифметическое")
choice = input("Введите номер операции(1, 2 или 3):")

if choice == '1':
    print(max(a, b, c))
elif choice == '2':
    print(min(a, b, c))
elif choice == '3':
    print((a + b + c)/ 3)

