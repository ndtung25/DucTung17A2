import math

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def perimeter(self):
        pass

    def area(self):
        pass


class Parallelogram(Polygon):
    def __init__(self, base, height):
        super().__init__(4)
        self.base = base
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.height)

    def area(self):
        return self.base * self.height


class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height)

    def perimeter(self):
        return 2 * (self.base + self.height)

    def area(self):
        return self.base * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def perimeter(self):
        return 4 * self.base

    def area(self):
        return self.base * self.base


def main():
    # Hình chữ nhật
    print("Nhập thông tin cho Hình Chữ Nhật:")
    width = float(input("Chiều rộng: "))
    height = float(input("Chiều cao: "))
    rectangle = Rectangle(width, height)
    print(f"Chu vi: {rectangle.perimeter()}")
    print(f"Diện tích: {rectangle.area()}")

    # Hình vuông
    print("\nNhập thông tin cho Hình Vuông:")
    side = float(input("Cạnh: "))
    square = Square(side)
    print(f"Chu vi: {square.perimeter()}")
    print(f"Diện tích: {square.area()}")

if __name__ == "__main__":
    main()
