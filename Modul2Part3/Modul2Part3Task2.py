number = float(input())

exponet = int(input())

if exponet < 0 or exponet > 7:
    print("Ошибка:степень должна быть от 0 до 7:")

else:
    result = number ** exponet
    print(f"{number} в степени {exponet} роавно {result} ")

