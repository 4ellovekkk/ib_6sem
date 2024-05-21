import string

# Настройка роторов и их начальных позиций
rotors = [
    {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H', 'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C', 'Z': 'J'},
    {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U', 'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H', 'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C', 'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N', 'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'E', 'Y': 'O', 'Z': 'V'},
    {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'C', 'Z': 'E'}
]

# Начальные позиции роторов
rotor_positions = [0, 0, 0]

# Рефлектор
reflector = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'}

def rotate_rotors():
    global rotor_positions
    rotor_positions[0] = (rotor_positions[0] + 1) % 26
    if rotor_positions[0] == 0:
        rotor_positions[1] = (rotor_positions[1] + 1) % 26
        if rotor_positions[1] == 0:
            rotor_positions[2] = (rotor_positions[2] + 1) % 26

def encrypt_char(char):
    global rotors, rotor_positions, reflector
    char = char.upper()
    if char not in string.ascii_uppercase:
        return char

    # Проход через роторы
    for i in range(3):
        char = rotors[i][char]
        char = chr((ord(char) - ord('A') + rotor_positions[i]) % 26 + ord('A'))

    # Проход через рефлектор
    char = reflector[char]

    # Проход обратно через роторы
    for i in range(2, -1, -1):
        char = chr((ord(char) - ord('A') - rotor_positions[i]) % 26 + ord('A'))
        char = {v: k for k, v in rotors[i].items()}[char]

    return char

def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        encrypted_message += encrypt_char(char)
        rotate_rotors()
    return encrypted_message
# Пример использования

def decipher_char(char):
    global rotors, rotor_positions, reflector
    char = char.upper()
    if char not in string.ascii_uppercase:
        return char

    # Проход через роторы в обратном порядке
    for i in range(2, -1, -1):
        char = chr((ord(char) - ord('A') - rotor_positions[i]) % 26 + ord('A'))
        char = {v: k for k, v in rotors[i].items()}[char]

    # Проход через рефлектор
    char = reflector[char]

    # Проход через роторы в прямом порядке
    for i in range(3):
        char = chr((ord(char) - ord('A') + rotor_positions[i]) % 26 + ord('A'))
        char = rotors[i][char]

    return char

def decipher_message(encrypted_message):
    global rotors, reflector, rotor_positions
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += decipher_char(char)
        rotate_rotors()
    return decrypted_message
message = "HELLO WORLD"
encrypted_message = encrypt_message(message)
print(f"Зашифрованное сообщение: {encrypted_message}")
print(f"Расшифрованное сообщение: {message}")