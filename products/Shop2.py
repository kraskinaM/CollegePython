products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80)],
    "Овощи": [("Морковь", 20, 30)],
    "Напитки": [("Чай", 25, 50), ("Кофе", 100, 10)],
    "Сбачки": [("Пушистые", 20, 30)]
}
print("Категории товаров:")
for category, items in products.items():
    print(f"{category}:")
    for item in items:
        name, quantity, price = item
        print(f"  {name} — {quantity} шт., {price} руб.")
most_expensive_item = None
for items in products.values():
    for item in items:
        if most_expensive_item is None or item[2] > most_expensive_item[2]:
            most_expensive_item = item
if most_expensive_item:
    print(f"\nСамый дорогой товар: {most_expensive_item[0]} — {most_expensive_item[2]} руб.")
max_quantity = 0
max_category = ""
for category, items in products.items():
    total_quantity = sum(item[1] for item in items)
    if total_quantity > max_quantity:
        max_quantity = total_quantity
        max_category = category
print(f"\nКатегория с наибольшим количеством товаров: {max_category} — {max_quantity} шт.")
total_cost = sum(item[1] * item[2] for items in products.values() for item in items)
print(f"\nОбщая стоимость всех товаров в магазине: {total_cost} руб.")