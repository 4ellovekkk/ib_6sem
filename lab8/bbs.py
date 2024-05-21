def bbs(p, q, x0, n):
    # Проверяем, что p и q удовлетворяют условиям Блюма
    if p % 4 != 3 or q % 4 != 3:
        raise ValueError("p и q должны быть простыми числами такими, что p ≡ q ≡ 3 (mod 4)")

    # Вычисляем N и начальное значение x
    N = p * q
    x = x0

    # Генерируем псевдослучайную последовательность
    result = []
    for _ in range(n):
        x = pow(x, 2, N)
        result.append(x % 2)

    return result

# Параметры
p = 17
q = 23
x0 = 19

# Генерируем последовательность
sequence = bbs(p, q, x0, 10)  # Генерация 10 битов
print("Generated sequence:", sequence)

# Выводим x1, x3, x7 и x10
x1 = sequence[0]
x3 = sequence[2]
x7 = sequence[6]
x10 = sequence[9]
print("x1:", x1)
print("x3:", x3)
print("x7:", x7)
print("x10:", x10)
