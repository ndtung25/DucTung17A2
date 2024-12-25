class TS():
    def __init__(self):
        self.thi_sinh_list = []
        while True:
            ten = input("Nhap ten thi sinh (Nhap 0 de ket thuc): ")
            if ten == "0":
                break
            toan = float(input("Nhap diem toan: "))
            li = float(input("Nhap diem ly: "))
            hoa = float(input("Nhap diem hoa: "))
            tong_diem = toan + li + hoa
            thi_sinh = {
                'ten': ten,
                'toan': toan,
                'li': li,
                'hoa': hoa,
                'tong_diem': tong_diem,
                'ket_qua': 'Do' if tong_diem > 20 else 'Truot'
            }
            self.thi_sinh_list.append(thi_sinh)

    def display(self):
        self.thi_sinh_list.sort(key=lambda x: x['tong_diem'], reverse=True)
        for thi_sinh in self.thi_sinh_list:
            print("Ten thi sinh: ", thi_sinh['ten'])
            print("Diem toan: ", thi_sinh['toan'])
            print("Diem ly: ", thi_sinh['li'])
            print("Diem hoa: ", thi_sinh['hoa'])
            print("Tong diem: ", thi_sinh['tong_diem'])
            print("Ket qua: ", thi_sinh['ket_qua'])
            print("---------------")

result = TS()
result.display()
