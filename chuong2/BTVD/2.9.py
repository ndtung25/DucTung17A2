import json
from collections import Counter

def read_company_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def employee_statistics(data):
    company_name = data['company_name']
    address = data['address']
    employees = data['employees']
    total_employees = len(employees)

    department_counts = Counter(emp['department'] for emp in employees)
    
    print(f"Tên công ty: {company_name}")
    print(f"Địa chỉ: {address}")
    print(f"Tổng số nhân viên: {total_employees}")
    print("-----Thống kê nhân viên theo đơn vị------")
    
    for i, (department, count) in enumerate(department_counts.items(), start=1):
        percentage = (count / total_employees) * 100
        print(f"{i}./Tên đơn vị: {department}. - Số nhân viên: {count} - Tỷ lệ: {percentage:.2f}%")

if __name__ == "__main__":
    data = read_company_data("company_data.json")
    employee_statistics(data)