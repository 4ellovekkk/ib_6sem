import time
import random
import sympy

# Функция для измерения времени вычисления y = (a^x) % n
def measure_mod_exp_time(a, x, n):
    start_time = time.time()
    y = pow(a, x, n)
    end_time = time.time()
    return end_time - start_time

# Параметры
a_values = [5, 35]  # Пример значений a
x_values = [sympy.prime(i) for i in range(26, 36)]  # Пример значений x (простые числа)
n_values = [sympy.randprime(2**1023, 2**1024), sympy.randprime(2**2047, 2**2048)]  # Пример значений n

# Результаты
results = []

for a in a_values:
    for x in x_values:
        for n in n_values:
            time_taken = measure_mod_exp_time(a, x, n)
            results.append((a, x, n.bit_length(), time_taken))

# Печать результатов
for result in results:
    print(f"a: {result[0]}, x: {result[1]}, n (bits): {result[2]}, time (s): {result[3]:.6f}")