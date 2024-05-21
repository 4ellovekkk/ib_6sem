from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes
import time

# Функция для разделения данных на блоки
def split_into_blocks(data, block_size):
    # Вычисляем количество блоков, которые будут созданы
    num_blocks = len(data) // block_size
    # Определяем, нужно ли добавить дополнение
    if len(data) % block_size != 0:
        num_blocks += 1
    # Создаем список для хранения блоков
    blocks = []
    # Разбиваем данные на блоки
    for i in range(num_blocks):
        start = i * block_size
        end = start + block_size
        block = data[start:end]
        # Если это последний блок и данные не делятся нацело, добавляем дополнение
        if i == num_blocks - 1 and len(block) < block_size:
            padding_length = block_size - len(block)
            padding = bytes([padding_length]) * padding_length
            block += padding
        blocks.append(block)
    return blocks

# Преобразование ключевой информации
def generate_key(surname):
    # Ensure the key length is suitable for Triple DES (either 16 or 24 bytes)
    key = surname.encode('utf-8')
    if len(key) < 16:
        # Pad the key to 16 bytes if it's shorter
        key = key.ljust(16, b'\0')
    elif len(key) > 24:
        # Truncate the key to 24 bytes if it's longer
        key = key[:24]
    return key


# Шифрование данных
def encrypt(data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    # Ensure the data is padded to the block size
    padded_data = pad_data(data, cipher.block_size)
    return cipher.encrypt(padded_data)

# Расшифрование данных
def decrypt(data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.decrypt(data)

# Замер времени выполнения операции
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# Функция для дополнения данных до кратного размера блока
def pad_data(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    return data + padding

# Функция для анализа лавинного эффекта
def avalanche_analysis(original_word, encrypted_word):
    # Реализация анализа лавинного эффекта
    pass

# Пример использования
if __name__ == "__main__":
    data = b"pivo pit vkusno zhit"  # Ваши данные
    key = generate_key("MAKAROV")  # Преобразуем вашу фамилию в ключ
    encrypted_data, encryption_time = measure_execution_time(encrypt, data, key)  # Шифруем данные
    decrypted_data, decryption_time = measure_execution_time(decrypt, encrypted_data, key)  # Расшифровываем данные

    print("Original Data:", data)
    print("Encrypted Data:", encrypted_data)
    print("Decrypted Data:", decrypted_data)

    print("Encryption Time:", encryption_time)
    print("Decryption Time:", decryption_time)

    # Пример анализа лавинного эффекта
    avalanche_analysis(data, encrypted_data)
