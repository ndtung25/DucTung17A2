import numpy as np
# 1. Tạo numpy array có giá trị từ 0-9
arr = np.arange(10)
print("Array ban đầu:", arr)
print("Kiểu dữ liệu của array:", arr.dtype)

# 2. Tạo arr_odd và arr_even
arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]
print("Array các số lẻ:", arr_odd)
print("Array các số chẵn:", arr_even)

# 3. Tạo arr_update_1 với số chẵn giữ nguyên, số lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 == 0, arr, 100)
print("Array sau khi cập nhật:", arr_update_1)
