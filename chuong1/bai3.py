class PS():
    def __init__(self):
        self.tu_so = float(input("Nhap tu so : "))
        self.mau_so = float(input("Nhap mau so : "))

        if self.mau_so == 0:
            print("Phan so khong hop le")
            self.phan_so = None
        else:
            self.phan_so = self.tu_so / self.mau_so
    def display(self):
        if self.phan_so is not None:
            print("Phan so da nhap : ", self.phan_so)

PS().display()