class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        return super().area()


class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        return super().area()


def main():
    # Nhập thông tin cho Tam Giác
    print("Nhập thông tin cho Tam Giác:")
    base = float(input("Cạnh đáy: "))
    height = float(input("Chiều cao: "))
    triangle = Triangle(base, height)
    print(f"Diện tích tam giác: {triangle.area()}")

    # Nhập thông tin cho Tam Giác Vuông
    print("\nNhập thông tin cho Tam Giác Vuông:")
    right_triangle = RightTriangle(base, height)
    print(f"Diện tích tam giác vuông: {right_triangle.area()}")

    # Nhập thông tin cho Tam Giác Cân
    print("\nNhập thông tin cho Tam Giác Cân:")
    isosceles_triangle = IsoscelesTriangle(base, height)
    print(f"Diện tích tam giác cân: {isosceles_triangle.area()}")

if __name__ == "__main__":
    main()
