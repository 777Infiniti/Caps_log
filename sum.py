class ComplexNumber:
    def __init__(self, real, imag):
        self.real = float(real)  # действительная часть
        self.imag = float(imag)  # мнимая часть

    def __add__(self, other):
        # Сложение комплексных чисел: (a + bi) + (c + di) = (a + c) + (b + d)i
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        # Форматирование вывода комплексного числа
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"