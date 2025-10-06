start = int(input("Введите начало диапазона:"))
end = int(input("Введите конец диапазона:"))

print("Все числа диапазона:")
for num in range(start, end+1):
    print(num,end="")
print()

print("Числа в убывающем порядке:")
for num in range(end, start-1, -1):
    print(num,end="")
print()

print("Числа кратные 7:")
for num in range(start,end +1):
   if num %7 == 0:
    print(num,end="")
print()


count_multiples_5 = 0
for num in range(start, end+1):
    if num % 5 == 0:
        count_multiples_5 += 1
print(f"Количество чисел кратных 5:,{count_multiples_5}")
