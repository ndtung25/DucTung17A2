import numpy as np

# Dữ liệu bài toán
arr_a = np.array([1, 2, 3, 2, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

common_elements = []
for elem in arr_a:
    if elem in arr_b and elem not in common_elements:
        common_elements.append(elem)
common_elements = np.array(common_elements)
print("Các phần tử xuất hiện ở cả hai mảng:", common_elements)

arr_c = []
for elem in arr_a:
    if elem not in arr_b and elem not in arr_c:
        arr_c.append(elem)
arr_c = np.array(arr_c)
print("Các phần tử chỉ xuất hiện trong arr_a:", arr_c)

arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = []
for elem in arr_e:
    if 5 <= elem <= 10:
        arr_f.append(elem)
arr_f = np.array(arr_f)
print("Các phần tử từ 5 đến 10 của arr_e:", arr_f)
