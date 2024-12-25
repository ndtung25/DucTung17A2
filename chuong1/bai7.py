class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        # Kiểm tra số ngày trong tháng
        if self.month in [1, 3, 5, 7, 8, 10]:
            days_in_month = 31
        elif self.month in [4, 6, 9, 11]:
            days_in_month = 30
        else:
            # Tháng 2
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                days_in_month = 29  # Năm nhuận
            else:
                days_in_month = 28  # Năm không nhuận

        # Tính ngày tiếp theo
        self.day += 1
        if self.day > days_in_month:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
