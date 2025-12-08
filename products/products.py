products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80)],
    "Овощи": [("Морковь", 20, 30)],
    "Напитки": [("Чай", 5, 70), ("Кофе", 2, 400)]
}
print("Каталог товаров:")
for category, items in products.items():
    print(f"{category}:")
    for name, qty, price in items:
        print(f"  - {name}: {qty} шт., {price} руб.")
print()
most_expensive = None
for category, items in products.items():
    for name, qty, price in items:
        if most_expensive is None or price > most_expensive[3]:
            most_expensive = (category, name, qty, price)
if most_expensive:
    cat, name, qty, price = most_expensive
    print(f"Самый дорогой товар во всём магазине: {name} (категория: {cat}), цена {price} руб., в наличии {qty} шт.")
else:
    print("Нет товаров.")
max_quantity_category = None
max_quantity = 0
for category, items in products.items():
    total_qty = sum(qty for _, qty, _ in items)
    if total_qty > max_quantity:
        max_quantity = total_qty
        max_quantity_category = category
if max_quantity_category:
    print(f"Категория с наибольшим количеством товаров: {max_quantity_category}, всего {max_quantity} шт.")
else:
    print("Нет категорий.")
total_value = 0
for items in products.values():
    for _, qty, price in items:
        total_value += qty * price
print(f"Общая стоимость всех товаров в магазине: {total_value} руб.")