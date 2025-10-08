total_sum = 0
max_number = None
min_number = None

while True:
    number = float(input())

    if number == 7:
        print("Good Bye")
        break
    else:
        total_sum += number

        if max_number is None or number > max_number:
            max_number = number

        if min_number is None or number < min_number:
            min_number = number

print(f"Сумма введенных чисел: {total_sum}")
if max_number is not None:
    print(f"Максимальное число: {max_number}")
if min_number is not None:
    print(f"Минимальное число: {min_number}")
