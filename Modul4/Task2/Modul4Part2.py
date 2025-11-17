import random
res = [random.randint(-2000,5000) for i in range(10)]
print("рандомный список чисел: "+str(res))
a = max(res)
print("максимальное число:",a)
b = min(res)
print("минимальное число:",b)
i = 0
print("сумма положительных чисел:",sum(i> 0 for i in res))
print("сумма отрицательных чисел:",sum(i < 0 for i in res))