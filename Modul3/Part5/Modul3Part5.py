def show_menu():
    print("\n" + "=" * 30)
    print("1. Прямоугольник")
    print("2. Треугольник")
    print("3. Пирамида")
    print("4. Квадрат")
    print("0. Выход")
    print("=" * 30)


while True:
    show_menu()
    choice = input("Выберите фигуру: ")

    if choice == '0':
        print("До свидания!")
        break
    elif choice == '1':
        w, h = int(input("Ширина: ")), int(input("Высота: "))
        for i in range(h):
            print('*' * w)
    elif choice == '2':
        h = int(input("Высота: "))
        for i in range(1, h + 1):
            print('*' * i)
    elif choice == '3':
        h = int(input("Высота: "))
        for i in range(1, h + 1):
            print(' ' * (h - i) + '*' * (2 * i - 1))
    elif choice == '4':
        s = int(input("Размер: "))
        for i in range(s):
            print('*' * s)
    else:
        print("Неверный выбор!")