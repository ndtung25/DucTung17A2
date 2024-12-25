import numpy as np
# 1. Tạo arr_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[5] = 1
print("Array sau khi cập nhật:", arr_zeros)

# 2. Tạo arr_h có giá trị từ 10 đến 24 và đảo ngược thứ tự
arr_h = np.arange(10, 25)
arr_h = arr_h[::-1]
print("Array đảo ngược:", arr_h)

# 3. Tạo arr_k từ array [1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0] với phần tử khác 0
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_k = arr_k[arr_k != 0]
print("Array với phần tử khác 0:", arr_k)

# 4. Thêm 2 phần tử có giá trị 10 và 20 vào cuối array arr_l
arr_l = np.array([1, 2, 3])
arr_l = np.append(arr_l, [10, 20])
print("Array sau khi thêm phần tử:", arr_l)

# 5. Cập nhật phần tử có giá trị 100 vào vị trí có index = 5
arr_l = np.array([1, 2, 3, 4, 5, 6])
arr_l[5] = 100
print("Array sau khi cập nhật index 5:", arr_l)

# 6. Xóa các phần tử tại vị trí index = 0, 1, 2
arr_l = np.delete(arr_l, [0, 1, 2])
print("Array sau khi xóa các phần tử:", arr_l)
