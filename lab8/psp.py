def polynomial_generator():
    # Коэффициенты полинома
    coefficients = [1, 0, 0, 1, 0, 0, 1]
    
    # Находим наименьшее общее кратное степеней x в полиноме
    lcm = 12
    
    # Генерируем начальную последовательность
    initial_sequence = [1, 1, 1, 0, 0, 0]
    
    # Генерируем значения полинома, начиная с начальной последовательности
    for x in range(lcm):
        value = sum(coefficient * (x ** degree) for degree, coefficient in enumerate(coefficients))
        yield bin(initial_sequence[x % len(initial_sequence)] + value)

# Используем генератор
for value in polynomial_generator():
    print(value)
