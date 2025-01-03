import sqlite3

# Kết nối với cơ sở dữ liệu (nếu không tồn tại, sẽ tạo mới)
conn = sqlite3.connect('product.db')
cursor = conn.cursor()

# Tạo bảng product
cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

def display_products():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    
    if products:
        print("\nDanh sách sản phẩm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        print("\nKhông có sản phẩm nào.")
    
    conn.close()

def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)', (name, price, amount))
    conn.commit()
    conn.close()

    print("Sản phẩm đã được thêm thành công.")

def search_product():
    name = input("Nhập tên sản phẩm cần tìm: ")

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + name + '%',))
    products = cursor.fetchall()

    if products:
        print("\nKết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        print("Không tìm thấy sản phẩm.")
    
    conn.close()

def update_product():
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE product SET Price = ?, Amount = ? WHERE Id = ?', (new_price, new_amount, product_id))
    conn.commit()
    conn.close()

    print("Thông tin sản phẩm đã được cập nhật.")

def delete_product():
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM product WHERE Id = ?', (product_id,))
    conn.commit()
    conn.close()

    print("Sản phẩm đã được xóa.")

def main_menu():
    while True:
        print("\n--- QUẢN LÝ SẢN PHẨM ---")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()