def is_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True
start = int(input())
end = int(input())

primes_in_range = []

for num in range(start, end+1):
    if is_prime(num):
        primes_in_range.append(num)

print(f" Простые числа в диапазоне от {start} до  {end} : {primes_in_range}")