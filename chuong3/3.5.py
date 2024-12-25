import numpy as np

# Đọc dữ liệu từ file
def read_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return [float(value.strip()) for value in data]

# Đọc dữ liệu chiều cao và cân nặng
heights = read_data('heights_1.txt')
weights = read_data('weights_1.txt')

# Tạo mảng NumPy
arr_height = np.array(heights)
arr_weight = np.array(weights)

print("Mảng chiều cao:")
print(arr_height)

print("\nMảng cân nặng:")
print(arr_weight)

# Tính toán BMI
arr_bmi = arr_weight / (arr_height ** 2)

# Lọc các cầu thủ có BMI >= 100
bmi_100_plus = arr_bmi[arr_bmi >= 100]

# Lọc các cầu thủ có chỉ số vị trí từ 100 đến 110
players_100_to_110 = arr_height[100:111]

# Tính chiều cao trung bình
avg_height = np.mean(arr_height)

# Tìm các cầu thủ có chiều cao >= chiều cao trung bình
tall_players = arr_height[arr_height >= avg_height]

# Tìm chiều cao và cân nặng lớn nhất
max_height = np.max(arr_height)
max_weight = np.max(arr_weight)

# Tìm chiều cao và cân nặng nhỏ nhất
min_height = np.min(arr_height)
min_weight = np.min(arr_weight)

# Tạo mảng các cặp (chiều cao, cân nặng)
height_weight_pairs = np.column_stack((arr_height, arr_weight))

# In kết quả
print("Chiều cao trung bình:", avg_height)
print("Cầu thủ cao nhất:", max_height)
print("Cầu thủ nặng nhất:", max_weight)
print("Cầu thủ thấp nhất:", min_height)
print("Cầu thủ nhẹ nhất:", min_weight)
print("Các cặp chiều cao và cân nặng:\n", height_weight_pairs)