# Класс Равнобочная трапеция, члены класса: координаты 4-х точек. Предусмотреть в
#  классе конструктор и методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления и вывода сведений о фигуре: длины сторон, периметр, площадь.
#  Продемонстрировать работу с классом: дано N трапеций, найти количество трапеций, у
#  которых площадь больше средней площади.


# PS Трапеция, боковые стороны которой равны, называется равнобедренной или 
# равнобокой. 


class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4

    def is_isosceles(self):
        side1 = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        side2 = ((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)**0.5
        side3 = ((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2)**0.5
        side4 = ((self.x1 - self.x4)**2 + (self.y1 - self.y4)**2)**0.5

        return side1 == side3 or side2 == side4

    def calculate_lengths(self):
        side1 = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        side2 = ((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)**0.5
        side3 = ((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2)**0.5
        side4 = ((self.x1 - self.x4)**2 + (self.y1 - self.y4)**2)**0.5

        return side1, side2, side3, side4

    def calculate_perimeter(self):
        side1, side2, side3, side4 = self.calculate_lengths()
        return side1 + side2 + side3 + side4

    def calculate_area(self):
        side1, side2, side3, side4 = self.calculate_lengths()
        s = (side1 + side3) / 2 * ((side2**2 - ((side1 - side3)**2 + side2**2 - side4**2) / (2 * (side1 - side3)))**0.5)
        return s

# Пример использования класса Trapezoid
trapezoid1 = Trapezoid(0, 0, 1, 2, 4, 2, 5, 0)
trapezoid2 = Trapezoid(0, 0, 1, 1, 3, 1, 4, 0)

trapezoids = [trapezoid1, trapezoid2]

total_area = sum(trapezoid.calculate_area() for trapezoid in trapezoids)
average_area = total_area / len(trapezoids)

count_greater_than_average = sum(1 for trapezoid in trapezoids if trapezoid.calculate_area() > average_area)

print("Количество трапеций, у которых площадь больше средней площади:", count_greater_than_average)