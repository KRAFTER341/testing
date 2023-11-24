# Класс Деньги для работы с денежными суммами. Число должно быть представлено
#  двумя полями: типа int для рублей и типа int - для копеек. Дробная часть (копейки) при
#  выводе на экран должна быть отделена от целой части запятой. Реализовать сложение,
#  вычитание, деление сумм, деление суммы на дробное число, умножение на дробное
#  число и операции сравнения. Проверить эти методы.

class Money:
    def __init__(self, rubles, kopecks):
        self.rubles = rubles
        self.kopecks = kopecks

    def __add__(self, other):
        result_rubles = self.rubles + other.rubles
        result_kopecks = self.kopecks + other.kopecks
        if result_kopecks >= 100:
            result_rubles += 1
            result_kopecks -= 100
        return Money(result_rubles, result_kopecks)

    def __sub__(self, other):
        result_rubles = self.rubles - other.rubles
        result_kopecks = self.kopecks - other.kopecks
        if result_kopecks < 0:
            result_rubles -= 1
            result_kopecks += 100
        return Money(result_rubles, result_kopecks)

    def __truediv__(self, other):
        total_self_kopecks = self.rubles * 100 + self.kopecks
        total_other_kopecks = other.rubles * 100 + other.kopecks
        result_kopecks = total_self_kopecks / total_other_kopecks * 100
        result_rubles = int(result_kopecks // 100)
        result_kopecks = int(result_kopecks % 100)
        return Money(result_rubles, result_kopecks)

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __lt__(self, other):
        return (self.rubles, self.kopecks) < (other.rubles, other.kopecks)

# Пример использования
money1 = Money(5, 75)
money2 = Money(3, 50)

sum_result_money = money1 + money2
print(f"Сложение: {sum_result_money.rubles},{sum_result_money.kopecks}")

diff_result_money = money1 - money2
print(f"Вычитание: {diff_result_money.rubles},{diff_result_money.kopecks}")

div_result_money = money1 / money2
print(f"Деление: {div_result_money.rubles},{div_result_money.kopecks}")

comparison_result_money = money1 == money2
print(f"Сравнение: {comparison_result_money}")