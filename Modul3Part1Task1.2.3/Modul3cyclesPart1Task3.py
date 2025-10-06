start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in range(start, end + 1):
  if num % 3 == 0 and num % 5 == 0:
      print("Fizz Buzz")
  elif num % 3 == 0:
      print("Fizz")
  elif num % 5 == 0:
      print("Buzz")
  else:
      print(num)