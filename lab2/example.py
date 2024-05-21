import base64


def custom_xor_base64(buffer_a, buffer_b):
    decoded_a = base64.b64decode(buffer_a)
    decoded_b = base64.b64decode(buffer_b)

    result = []
    min_length = min(len(decoded_a), len(decoded_b))
    for i in range(min_length):
        result.append(chr(decoded_a[i] ^ decoded_b[i]))
    return "".join(result)


# Example usage
part_1 = "Makarov "
encoded_part_1 = base64.b64encode(part_1.encode()).decode()
print(encoded_part_1)

part_2 = "Alexey"
encoded_part_2 = base64.b64encode(part_2.encode()).decode()
print(encoded_part_2)


result = custom_xor_base64(encoded_part_1, encoded_part_2)
print(result)
