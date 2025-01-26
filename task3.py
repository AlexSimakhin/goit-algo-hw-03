"""task3.py"""
import logging

def hanoi(n, source, target, auxiliary):
    # Функція для вирішення задачі Ханоя
    if n == 1:
        logging.info(f"Перемістити диск 1 з {source} до {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)  # Рекурсивний виклик для переміщення n-1 дисків
        logging.info(f"Перемістити диск {n} з {source} до {target}")
        hanoi(n - 1, auxiliary, target, source)  # Другий рекурсивний виклик для залишку дисків

def main():
    try:
        # Введення кількості дисків
        n = int(input("Введіть кількість дисків: "))
        if n <= 0:
            raise ValueError("Кількість дисків повинна бути позитивним цілим числом.")
    except ValueError as e:
        # Обробка помилки, якщо введено некоректне значення
        print(f"Невірний ввід: {e}")
        return

    # Налаштовуємо логування
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Викликаємо функцію для вирішення задачі Ханоя
    hanoi(n, "A", "C", "B")
    print("Усі диски були успішно переміщені!")

if __name__ == "__main__":
    main()
