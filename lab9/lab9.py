import base64
import string
import random
import time

def generate_superincreasing_sequence(z, length):
    sequence = []
    for i in range(length):
        next_element = random.randint(1, 2**z - 1) + sum(sequence)
        sequence.append(next_element)
    return sequence

def generate_normal_sequence(superincreasing_sequence):
    normal_sequence = []
    for i in range(len(superincreasing_sequence)):
        normal_sequence.append(superincreasing_sequence[i] * (i + 1))
    return normal_sequence

def encode_message(message, encoding_type):
    if encoding_type == "Base64":
        encoded_message = base64.b64encode(message.encode()).decode()
    elif encoding_type == "ASCII":
        encoded_message = ''.join([str(ord(char)) for char in message])
    return encoded_message

def decode_message(encoded_message, encoding_type):
    if encoding_type == "Base64":
        decoded_message = base64.b64decode(encoded_message).decode()
    elif encoding_type == "ASCII":
        decoded_message = ''.join([chr(int(encoded_message[i:i+3])) for i in range(0, len(encoded_message), 3)])
    return decoded_message

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Генерация сверхвозрастающей последовательности
z = 6  # или 8 для ASCII
superincreasing_sequence = generate_superincreasing_sequence(z, length=10)

# Генерация нормальной последовательности
normal_sequence = generate_normal_sequence(superincreasing_sequence)

# Шифрование сообщения
message = "Иванов Иван Иванович"
encoded_message_base64 = encode_message(message, "Base64")
encoded_message_ascii = encode_message(message, "ASCII")

# Расшифрование сообщения
decoded_message_base64 = decode_message(encoded_message_base64, "Base64")
decoded_message_ascii = decode_message(encoded_message_ascii, "ASCII")

# Оценка времени выполнения операций
decoded_message, decoding_time = measure_time(decode_message, encoded_message_base64, "Base64")
encoded_message, encoding_time = measure_time(encode_message, message, "Base64")

print("Decoded message (Base64):", decoded_message)
print("Decoding time (Base64):", decoding_time)
print("Encoded message (Base64):", encoded_message_base64)
print("Encoding time (Base64):", encoding_time)
