from Crypto.Cipher import ARC4
import time

# Алгоритм RC4
def rc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext)

# Оценка скорости выполнения операций генерации ПСП
def evaluate_rc4_speed():
    key = b'\x14\x15\x16\x17\x3C\x3D'
    plaintext = b'Hello, world!'

    start_time = time.time()
    rc4_encrypt(key, plaintext)
    end_time = time.time()

    return end_time - start_time

# Пример использования
encryption_time = evaluate_rc4_speed()
print("Время выполнения операции генерации ПСП:", encryption_time, "секунд")
