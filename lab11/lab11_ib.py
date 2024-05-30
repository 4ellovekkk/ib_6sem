import hashlib
import time


def hash_message(message: str) -> str:
    """Функция для хеширования сообщения с использованием SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return sha256.hexdigest()


def evaluate_performance(message: str, iterations: int) -> None:
    """Функция для оценки быстродействия алгоритма хеширования."""
    start_time = time.time()

    for _ in range(iterations):
        hash_message(message)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время, затраченное на {iterations} итераций: {elapsed_time:.6f} секунд")
    print(f"Среднее время на итерацию: {elapsed_time / iterations:.6f} секунд")


if __name__ == "__main__":
    input_message = input("Введите сообщение для хеширования: ")
    iterations = int(
        input("Введите количество итераций для оценки быстродействия: "))

    # Хеширование сообщения
    hash_result = hash_message(input_message)
    print(f"Хешированное сообщение (SHA-256): {hash_result}")

    # Оценка быстродействия
    evaluate_performance(input_message, iterations)
