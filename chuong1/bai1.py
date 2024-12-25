class Hcn():
    def __init__(self):
        self.dai = float(input("Nhap chieu dai :"))
        self.rong = float(input("Nhap chieu rong :"))
        s = self.dai * self.rong
        p = (self.dai + self.rong) * 2
        self.s = s
        self.p = p

    def display(self):
        print("Chieu dai: ", self.dai)
        print("Chieu rong:", self.rong)
        print("Dien tich: ", self.s)
        print("Chu vi: ", self.p)
        
Hcn().display()