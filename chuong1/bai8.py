class Employee:
    def __init__(self, name, birth_date, joining_date):
        self.name = name
        self.birth_date = birth_date  # Kiểu Date
        self.joining_date = joining_date  # Kiểu Date

    def display_info(self):
        print(f"Tên nhân viên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.joining_date.display()
# Chuong trinh quan li nhan vien
def main():
    employees = []
    
    # Nhập thông tin nhân viên
    while True:
        name = input("Nhập tên nhân viên (hoặc 'exit' để thoát): ")
        if name.lower() == 'exit':
            break
        
        day_of_birth = int(input("Nhập ngày sinh: "))
        month_of_birth = int(input("Nhập tháng sinh: "))
        year_of_birth = int(input("Nhập năm sinh: "))
        birth_date = Date(day_of_birth, month_of_birth, year_of_birth)
        
        day_of_joining = int(input("Nhập ngày vào công ty: "))
        month_of_joining = int(input("Nhập tháng vào công ty: "))
        year_of_joining = int(input("Nhập năm vào công ty: "))
        joining_date = Date(day_of_joining, month_of_joining, year_of_joining)
        
        employee = Employee(name, birth_date, joining_date)
        employees.append(employee)

    # Hiển thị thông tin nhân viên
    print("\nDanh sách nhân viên:")
    for emp in employees:
        emp.display_info()
        print("--------------------------")

if __name__ == "__main__":
    main()
