def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission = sales * 0.03
    elif sales <= 1000:
        commission = sales * 0.05
    else:
        commission = sales * 0.08
    total_salary = base_salary + commission
    return total_salary
sales1 = float(input("Ведите уровень продаж для менеджера 1:"))
sales2 = float(input("Введите уровень продаж для менеджера 2:"))
sales3 = float(input("Введите уровень продаж для менеджера 3:"))
salary1 = calculate_salary(sales1)
salary2 = calculate_salary(sales2)
salary3 = calculate_salary(sales3)
max_salary = salary1
best_manager = 1
if salary2 > max_salary:
    max_salary = salary2
    best_manager = 2
if salary3 > max_salary:
    max_salary = salary3
    best_manager = 3
if best_manager == 1:
    salary1 += 200
elif best_manager == 2:
    salary2 += 200
else:
    salary3 += 200
print("Итоговаые зарплаты менеджеров:")
print(f"Менеджер 1 : {sales1}")
print(f"Менеджер 2 : {sales2}")
print(f"Менеджер 3 : {sales3}")
print(f"Лучший менеджер: Менеджер {best_manager} (премия 200$ начисления )")
