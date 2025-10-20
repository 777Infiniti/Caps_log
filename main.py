import math

try:
    # Запрашиваем у пользователя число
    number = float(input("Введите число: "))
    
    # Вычисляем квадратный корень
    if number >= 0:
        square_root = math.sqrt(number)
        print(f"Квадратный корень из {number} равен {square_root}")
    else:
        print("Невозможно вычислить квадратный корень из отрицательного числа.")
    
    # Вычисляем обратную величину
    if number != 0:
        inverse_value = 1 / number
        print(f"Обратная величина для {number} равна {inverse_value}")
    else:
        print("Невозможно вычислить обратную величину для нуля.")
        
except ValueError:
    print("Ошибка: введено некорректное число.")
