# Q1 - Base class - Polygon : 2 methods, input(sides) and display()
# Derived class - Triangle : 2 methods, area() and perimeter()
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display(self):
        print("Polygon with", len(self.sides), "sides")


class Triangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def perimeter(self):
        return sum(self.sides)


t = Triangle([3, 4, 5])
t.display()
print("Area:", t.area())
print("Perimeter:", t.perimeter())