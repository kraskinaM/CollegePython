tariffs = {
    "MTC" : 1.5,
    "Билайн" : 1.2,
    "Мегафон": 1.3,
    "Теле2": 1.0
}

cost_per_minute = float(input("Введите стоимость разговора за минуту: "))

print("Доступные операторы:")
for operator in tariffs.keys():
    print(operator)

from_operator = input("Введите оператора с которого вы звоните: ")
to_operator = input("Введите оператора на который звоните: ")

if from_operator not in tariffs or to_operator not in tariffs:
    print("Ошибка один из введеных операторов не найден")

else:
    total_cost = cost_per_minute * (tariffs[to_operator] / tariffs[from_operator])

    print(f"Стоимость разговора с {from_operator} на {to_operator}: {total_cost:.2f} руб")