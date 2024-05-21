import base64
import collections
import math


def convert_to_base64(filename):
    with open(filename, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    return encoded_string.decode()


def calculate_entropy(text):
    frequencies = collections.Counter(text)
    entropy = 0.0
    total_length = len(text)
    for freq in frequencies.values():
        probability = freq / total_length
        entropy -= probability * math.log2(probability)
    return entropy


def calculate_redundancy(text):
    frequencies = collections.Counter(text)
    total_length = len(text)
    max_entropy = math.log2(len(frequencies))

    actual_entropy = 0.0
    for freq in frequencies.values():
        probability = freq / total_length
        actual_entropy -= probability * math.log2(probability)

    redundancy = (max_entropy - actual_entropy) / max_entropy
    return redundancy


def custom_xor_base64(buffer_a, buffer_b):
    decoded_a = base64.b64decode(buffer_a)
    decoded_b = base64.b64decode(buffer_b)

    result = []
    min_length = min(len(decoded_a), len(decoded_b))
    for i in range(min_length):
        result.append(chr(decoded_a[i] ^ decoded_b[i]))
    return "".join(result)


def custom_xor_ascii(string_a, string_b):
    # Преобразование строк в коды ASCII
    ascii_a = [ord(char) for char in string_a]
    ascii_b = [ord(char) for char in string_b]

    # Выполнение операции XOR
    result = []
    min_length = min(len(ascii_a), len(ascii_b))
    for i in range(min_length):
        result.append(chr(ascii_a[i] ^ ascii_b[i]))
    return "".join(result)


file_name = "latin_text.txt"  # Название вашего текстового документа
base64_content = convert_to_base64(file_name)
with open("base64_res.txt", "w") as file:
    file.write(base64_content)

with open("latin_text.txt", "r") as file:
    text = file.read()
print(f"избыточность base64: {calculate_redundancy(base64_content)}")
print(f"избыточность латинский алфавит: {calculate_redundancy(text)}")

part_1 = "Makarov "
encoded_part_1 = base64.b64encode(part_1.encode()).decode()
print(f"закодированная часть 1: {encoded_part_1}")
part_2 = "Alexey"
encoded_part_2 = base64.b64encode(part_2.encode()).decode()
print(f"закодированная часть 2: {encoded_part_2}")
result = custom_xor_base64(encoded_part_1, encoded_part_2)
print(f"xor base64 {result}")

print(f"xor ascii: {custom_xor_ascii(part_1,part_2)}")
