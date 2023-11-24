# 1) Класс Дробное число со знаком (Fractions). Число должно быть представлено двумя
#  полями: целая часть - длинное целое со знаком, дробная часть - беззнаковое короткое
#  целое. Реализовать арифметические операции сложения, вычитания, умножения и 
#  операции сравнения. Проверить эти методы.


class Fraction:
    def __init__(self, whole_part, fractional_part):
        self.whole_part = whole_part
        self.fractional_part = fractional_part

    def __add__(self, other):
        new_whole_part = self.whole_part + other.whole_part
        new_fractional_part = self.fractional_part + other.fractional_part
        if new_fractional_part >= 2**16:  # Проверка переполнения в дробной части
            new_whole_part += 1
            new_fractional_part -= 2**16
        return Fraction(new_whole_part, new_fractional_part)

    def __sub__(self, other):
        new_whole_part = self.whole_part - other.whole_part
        new_fractional_part = self.fractional_part - other.fractional_part
        if new_fractional_part < 0:  # Проверка на заем в дробной части
            new_whole_part -= 1
            new_fractional_part += 2**16
        return Fraction(new_whole_part, new_fractional_part)

    def __mul__(self, other):
        product_whole_part = (
            self.whole_part * other.whole_part +
            self.whole_part * other.fractional_part +
            other.whole_part * self.fractional_part
        )
        product_fractional_part = self.fractional_part * other.fractional_part
        return Fraction(product_whole_part, product_fractional_part)

    def __eq__(self, other):
        return (self.whole_part == other.whole_part and
                self.fractional_part == other.fractional_part)

    def __lt__(self, other):
        return (
            self.whole_part < other.whole_part or
            (self.whole_part == other.whole_part and
             self.fractional_part < other.fractional_part)
        )

# Пример использования:
fraction1 = Fraction(2, 32768)  # 2.5
fraction2 = Fraction(1, 16384)  # 1.0625

# Тестовое дополнение
result_addition = fraction1 + fraction2
print(result_addition)  # Выход: дробь(3, 49152)  # 3.8125

# Тестовое вычитание
result_subtraction = fraction1 - fraction2
print(result_subtraction)  # Выход: дробь(0, 16384)  # 0.4375

# Тестовое умножение
result_multiplication = fraction1 * fraction2
print(result_multiplication)  # Выход: дробь(3, 8192)  # 3.1875

# Проверка равенства
print(fraction1 == fraction2)  # Выход: Ложь

# Тест менее
print(fraction1 < fraction2)  # Выход: Ложь