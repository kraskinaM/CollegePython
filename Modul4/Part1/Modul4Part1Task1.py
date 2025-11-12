string = input("Введите строку: ")
reversed_string = string[::-1]
if string == reversed_string:
   print("Строка является палиндромом")
else:
   print("Строка не является палиндромом")
