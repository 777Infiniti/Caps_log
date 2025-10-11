def calculator():
    print("Операции: +, -, *, /")
    num1 = float(input("Первое число: "))
    op = input("Операция: ")
    num2 = float(input("Второе число: "))
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2 if num2 != 0 else "Ошибка: деление на 0"
    else:
        result = "Неверная операция"
    print(f"Результат: {result}")

calculator()