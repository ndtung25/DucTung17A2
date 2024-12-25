import numpy as np

# Tạo mảng 2D ngẫu nhiên
arr_2d = np.random.randint(1, 10, size=(3, 3))
print("Mảng 2D ban đầu:\n", arr_2d)

# Chuyển vị mảng
arr_2d_transpose = arr_2d.T
print("Mảng 2D sau khi chuyển vị:\n", arr_2d_transpose)

# Sắp xếp các dòng theo thứ tự tăng dần
arr_2d_sorted_rows = np.sort(arr_2d, axis=0)
print("Mảng 2D sau khi sắp xếp các dòng:\n", arr_2d_sorted_rows)

# Sắp xếp các cột theo thứ tự giảm dần
arr_2d_sorted_cols = np.sort(arr_2d, axis=1)[::-1]
print("Mảng 2D sau khi sắp xếp các cột:\n", arr_2d_sorted_cols)

# Tìm kiếm các phần tử có giá trị bằng 5
indices = np.where(arr_2d == 5)
print("Vị trí của các phần tử có giá trị 5:", indices)

# Kiểm tra xem trong mảng có phần tử nào bằng 3 không
has_value_3 = np.any(arr_2d == 3)
print("Có phần tử nào bằng 3 không:", has_value_3)