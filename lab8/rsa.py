from Crypto.PublicKey import RSA
import Crypto.Util.number

# Генерация ключей RSA
def generate_RSA_keys():
    # Генерация случайного простого числа p и q
    p = Crypto.Util.number.getPrime(256)
    q = Crypto.Util.number.getPrime(256)

    # Выбор открытой экспоненты e
    e = 65537

    # Вычисление модуля n
    n = p * q

    # Вычисление функции Эйлера
    phi = (p - 1) * (q - 1)

    # Вычисление секретной экспоненты d
    d = Crypto.Util.number.inverse(e, phi)

    # Создание объекта ключа RSA
    key = RSA.construct((n, e, d))

    return key

# Пример использования
key = generate_RSA_keys()
print("Открытый ключ (n, e):", key.n, key.e)
print("Закрытый ключ (d):", key.d)
