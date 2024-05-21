import matplotlib.pyplot as plt
import numpy as np
import math


def calculate_entropy(text):
    # Подсчет частоты появления каждого символа
    char_freq = {}
    total_chars = len(text)
    for char in text:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

    # Рассчет вероятности для каждого символа
    probabilities = {char: freq / total_chars for char, freq in char_freq.items()}

    # Рассчет энтропии
    entropy = -sum(p * math.log2(p) for p in probabilities.values() if p != 0)
    return entropy


def calculate_entropy_graph(text):
    # Подсчет частоты появления каждого символа
    char_freq = {}
    total_chars = len(text)
    for char in text:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

    # Рассчет вероятности для каждого символа
    probabilities = {char: freq / total_chars for char, freq in char_freq.items()}

    # Построение гистограммы
    plt.figure(figsize=(10, 6))
    plt.bar(probabilities.keys(), probabilities.values())
    plt.title("Гистограмма частоты символов")
    plt.xlabel("Символы")
    plt.ylabel("Вероятности")
    plt.xticks(rotation=90)
    plt.show()

    # Рассчет энтропии
    entropy = -sum(p * math.log2(p) for p in probabilities.values() if p != 0)
    print("Энтропия:", entropy)
    return entropy


def is_binary(text):
    for char in text:
        if char not in ["0", "1"]:
            return False
    return True


def effective_entropy(text, p):
    q = 1 - p
    if is_binary(text) and (p == 0 or q == 0):
        return 1
    elif q == 0:
        return 1
    else:
        return calculate_entropy(text) - (-p * math.log2(p) - q * math.log2(q))


def info_amount_with_errors(file, p):
    try:
        with open(file, "r") as f:
            text = f.read()
        return effective_entropy(text, p) * len(text)
    except FileNotFoundError:
        return None


error_probabilities = [0.1, 0.5, 1.0]
# Обработка текста на латинице
with open("latin_text.txt", "r", encoding="utf-8") as file:
    latin_text = file.read()
print("Для текста на латинице:")
lat_ent = calculate_entropy_graph(latin_text)

# Обработка текста на русском
with open("base64_res.txt", "r", encoding="utf-8") as file:
    cyrillic_text = file.read()
print("\nДля текста base64:")
cyr_entr = calculate_entropy_graph(cyrillic_text)
