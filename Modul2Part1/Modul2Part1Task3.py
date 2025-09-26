meters = float(input())

print("Выберите единицу для перевода:")
print("1 - Мили ")
print("2 - Дюймы ")
print("3 - Ярды ")
choice = input("Введите номер операции (1, 2 или 3):")

if choice == '1':
    miles = meters * 0.000621371
    print(f"{meters} = {miles} ")
elif choice == '2':
    inches = meters * 39.3701
    print(f"{meters} = {inches} ")
elif choice == '3':
    yards = meters * 1.0936
    print(f"{meters} = {yards} ")