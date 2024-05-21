def snake_permutation(text):
    """
    Переставляет текст в змейку.
    """
    rows = int(len(text) ** 0.5)
    if rows * rows < len(text):
        rows += 1
    columns = rows
    matrix = [['' for _ in range(columns)] for _ in range(rows)]
    direction = 0 # 0 - вправо, 1 - вниз
    row, col = 0, 0
    for char in text:
        matrix[row][col] = char
        if direction == 0:
            if col == columns - 1:
                direction = 1
                row += 1
            else:
                col += 1
        else:
            if row == rows - 1:
                direction = 0
                col += 1
            else:
                row += 1
    return ''.join([''.join(row) for row in matrix])


def encrypt_snake(text):
    """
    Шифрует текст с использованием маршрутной перестановки "змейка".
    """
    snake_text = snake_permutation(text)
    encrypted_text = ''.join(chr((ord(char) - ord('A') + 1) % 26 + ord('A')) for char in snake_text)
    return encrypted_text

def decrypt_snake(encrypted_text):
    """
    Расшифровывает текст, зашифрованный с использованием маршрутной перестановки "змейка".
    """
    snake_text = ''.join(chr((ord(char) - ord('A') - 1) % 26 + ord('A')) for char in encrypted_text)
    original_text = snake_permutation(snake_text)
    return original_text

def permute_text(text, keyword):
    """
    Переставляет символы в тексте в соответствии с ключевым словом.
    """
    # Создаем словарь для хранения позиций символов в ключевом слове
    keyword_dict = {char: index for index, char in enumerate(keyword)}
    
    # Сортируем символы текста по их позициям в ключевом слове
    sorted_text = ''.join(sorted(text, key=lambda char: keyword_dict.get(char, len(keyword))))
    
    return sorted_text


def encrypt_with_keyword(text, keyword):
    """
    Шифрует текст с использованием метода множественной перестановки с ключевым словом.
    """
    permuted_text = permute_text(text, keyword)
    encrypted_text = ''.join(chr((ord(char) - ord('A') + 1) % 26 + ord('A')) for char in permuted_text)
    return encrypted_text

def decrypt_with_keyword(encrypted_text, keyword):
    """
    Расшифровывает текст, зашифрованный с использованием метода множественной перестановки с ключевым словом.
    """
    permuted_text = ''.join(chr((ord(char) - ord('A') - 1) % 26 + ord('A')) for char in encrypted_text)
    original_text = permute_text(permuted_text, keyword)
    return original_text[::-1]


text = "HELLO"
print("исходный текст: ",text)
print("змейка:")
encrypted_text = encrypt_snake(text)
print(f"Зашифрованный текст: {encrypted_text}")

decrypted_text = decrypt_snake(encrypted_text)
print(f"Расшифрованный текст: {decrypted_text}")


keyword = "MAKAROVALEXEY"
encrypted_text = encrypt_with_keyword(text, keyword)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = decrypt_with_keyword(encrypted_text, keyword)
print(f"Расшифрованный текст: {decrypted_text}")