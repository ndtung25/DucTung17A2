import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Ellipse(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a  # Bán trục lớn
        self.b = b  # Bán trục nhỏ

    def area(self):
        return math.pi * self.a * self.b


class Circle(Ellipse):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)

    def area(self):
        return math.pi * self.a ** 2


def main():
    # Nhập thông tin cho Elip
    print("Nhập thông tin cho Elip:")
    a = float(input("Bán trục lớn: "))
    b = float(input("Bán trục nhỏ: "))
    ellipse = Ellipse(0, 0, a, b)
    print(f"Diện tích elip: {ellipse.area()}")

    # Nhập thông tin cho Đường Tròn
    print("\nNhập thông tin cho Đường Tròn:")
    radius = float(input("Bán kính: "))
    circle = Circle(0, 0, radius)
    print(f"Diện tích đường tròn: {circle.area()}")

if __name__ == "__main__":
    main()
