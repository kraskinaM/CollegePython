num1 = int(input("Введите первое число "))
num2 = int(input("Введите второе число "))

def print_multiplication_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")

print(f"\nТаблица умножения для {num1}:")
print_multiplication_table(num1)

print(f"\nТаблица умножения для {num2}:")
print_multiplication_table(num2)