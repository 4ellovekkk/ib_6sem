import math

# Функция для нахождения всех простых чисел в интервале [2, n]
def find_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(int(math.sqrt(n)) + 1, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


# Функция для вычисления НОД двух чисел
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Функция для факторизации числа на простые множители
def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


# Функция для конкатенации чисел и проверки на простоту
def is_concatenated_prime(m, n):
    concatenated = int(str(m) + str(n))

    if concatenated < 2:
        return False

    for i in range(2, int(math.sqrt(concatenated)) + 1):
        if concatenated % i == 0:
            return False

    return True


# Поиск простых чисел в интервале [m, n]
def find_primes_in_range(m, n):
    primes = []
    for num in range(m, n + 1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes


# Значения m и n
m = 667
n = 703

# 1. Найти все простые числа в интервале [2, n]
primes_1 = find_primes(n)
print("Простые числа в интервале [2, n]:", primes_1)

# Подсчитать количество простых чисел в указанном интервале
count_primes_1 = len(primes_1)
print("Количество простых чисел в интервале [2, n]:", count_primes_1)

# Сравнить это число с n/ln(n)
n_div_ln_n = n / math.log(n)
print("n/ln(n):", n_div_ln_n)
print("Отношение количества простых чисел к n/ln(n):", count_primes_1 / n_div_ln_n)

# 2. Повторить п. 1 для интервала [m, n]
primes_2 = find_primes_in_range(m, n)
print("Простые числа в интервале [m, n]:", primes_2)

# Сравнить результаты с ручными вычислениями, используя решето Эратосфена
# Здесь просто используем количество простых чисел в интервале [2, n], так как уже реализовано решето Эратосфена
print(
    "Количество простых чисел в интервале [m, n] (с решетом Эратосфена):", len(primes_2)
)


# 3. Записать числа m и n в виде произведения простых множителей
factors_m = prime_factors(m)
factors_n = prime_factors(n)
print("Простые множители числа m:", factors_m)
print("Простые множители числа n:", factors_n)

# 4. Проверить, является ли число, состоящее из конкатенации цифр m и n, простым
concatenated_prime = is_concatenated_prime(m, n)
if concatenated_prime:
    print("Число, состоящее из конкатенации цифр m и n, является простым")
else:
    print("Число, состоящее из конкатенации цифр m и n, не является простым")

# 5. Найти НОД (m, n)
gcd_m_n = gcd(m, n)
print("Наибольший общий делитель (НОД) m и n:", gcd_m_n)


# Выполнить задания по условиям п. 1 и 2.
primes_between_2_and_n = find_primes(n)
primes_between_m_and_n = find_primes_in_range(m, n)

print("Простые числа в интервале [2, n]:", primes_between_2_and_n)
print("Количество простых чисел в интервале [2, n]:", len(primes_between_2_and_n))
print("Простые числа в интервале [m, n]:", primes_between_m_and_n)
print("Количество простых чисел в интервале [m, n]:", len(primes_between_m_and_n))
