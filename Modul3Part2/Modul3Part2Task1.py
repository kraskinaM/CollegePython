start = int(input("Введите первое число: "))
end = int(input("Введите второе число: "))
even_sum = odd_sum = miltiples_of_nine_sum = 0
even_count = odd_count = miltiples_of_nine_count = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1
    if num % 9 == 0:
        miltiples_of_nine_sum += num
        miltiples_of_nine_count += 1

print(f"Четные: {even_sum} Ср.:{even_sum / even_count if even_count > 0 else 0}")
print(f"Нечетные: {odd_count} Ср.:{odd_count / odd_count if odd_count else 0} ")
print(f"Кратные 9: {miltiples_of_nine_sum} Ср.: {miltiples_of_nine_sum / miltiples_of_nine_count if miltiples_of_nine_count else 0}")
