'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(numbers[0], len(numbers)+1):
    for k in range(numbers[1], len(numbers)+1):
        #if i // k == 0:
           # primes.append(numbers)
            print(primes)'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:  # Перебираем каждое число в списке
    if num < 2:  # Числа меньше 2 не являются простыми
        not_primes.append(num)
        continue

    is_prime = True  # Предполагаем, что число простое
    for i in range(2, int(num ** 0.5) + 1):  # Проверяем делимость
        if num % i == 0:  # Если число делится на i, оно не простое
            is_prime = False
            break  # Прерываем внутренний цикл

    if is_prime:  # Если число простое, добавляем в массив primes
        primes.append(num)
    else:  # Если число не простое, добавляем в массив not_primes
        not_primes.append(num)

print("Простые числа:", primes)
print("Непростые числа:", not_primes)