products = {
    "Tелефон": frozenset(("iPhone", "Samsung")),
    "Чулки": frozenset(("Мужские", "Женские")),
}
while True:
    print("\nМеню:")
    print("1. Добавить товар")
    print("2. Вывести все товары")
    print("3. Найти товары по категории")
    print("4. Выйти")
    choice = input("Выберите пункт: ").strip()
    if choice == "1":
        name = input("Название товара: ").strip()
        if not name:
            print("Пустое название — отмена.")
            continue
        cats = input("Категории (через запятую): ").strip()
        categories = frozenset([c.strip() for c in cats.split(",") if c.strip()]) if cats else frozenset()
        products[name] = categories
        print("Добавлено.")
    elif choice == "2":
        for name in sorted(products.keys(), key=lambda s: len(s)):
            print(f"- {name}: {', '.join(sorted(products[name]))}")
    elif choice == "3":
        cat = input("Введите категорию для поиска: ").strip()
        result = {name for name, cats in products.items() if cat in cats}
        if result:
            print("Найдено:")
            for name in sorted(result, key=lambda s: len(s)):
                print(f"- {name}")
        else:
            print("Товаров с такой категорией не найдено.")
    elif choice == "4":
        print("Выход.")
        break
    else:
        print("Неверный пункт. Повторите.")