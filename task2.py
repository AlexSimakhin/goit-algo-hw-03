"""task2.py"""
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)  # Якщо рівень рекурсії 0, малюємо відрізок
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)  # Рекурсивно малюємо частину кривої
            t.left(angle)  # Повороти для створення фрагмента кривої

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)  # Малюємо одну зі сторін сніжинки
        t.right(120)  # Поворот на 120° після кожної сторони

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()  # Створення екрану для малювання
    window.bgcolor("white")  # Встановлення білого фону

    t = turtle.Turtle()  # Створення черепахи для малювання
    t.speed(0)  # Встановлення максимальної швидкості малювання
    t.penup()  # Підйом пера, щоб не малювати лінію при переміщенні
    t.goto(-size / 2, size / 3)  # Переміщення черепахи в початкову позицію
    t.pendown()  # Встановлення пера вниз для малювання

    koch_snowflake(t, order, size)  # Малюємо фрактал сніжинки

    window.mainloop()  # Оновлення екрану і очікування завершення малювання

if __name__ == "__main__":
    try:
        order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))  # Введення рівня рекурсії
        draw_koch_snowflake(order)  # Виклик функції для малювання сніжинки
    except ValueError:
        print("Невірний ввід. Будь ласка, введіть коректне ціле число для рівня рекурсії.")  # Обробка помилки при введенні
