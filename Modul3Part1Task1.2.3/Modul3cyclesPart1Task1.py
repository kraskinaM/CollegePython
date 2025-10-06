start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)