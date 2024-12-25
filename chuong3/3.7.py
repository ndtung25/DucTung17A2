import numpy as np

# Hàm đọc dữ liệu từ file
def read_baseball_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    # Loại bỏ ký tự xuống dòng và tách thành các cặp (chiều cao, cân nặng)
    data = [tuple(map(float, line.strip().split())) for line in data]
    return data

# Đọc dữ liệu từ file
baseball_data = read_baseball_data('baseball_2D.txt')

# Chuyển đổi dữ liệu thành mảng NumPy
baseball_np = np.array(baseball_data)

# Chia mảng thành 2 mảng riêng biệt cho chiều cao và cân nặng
height, weight = baseball_np[:, 0], baseball_np[:, 1]

# Thực hiện các phép tính thống kê
avg_height = np.mean(height)
avg_weight = np.mean(weight)
std_height = np.std(height)
std_weight = np.std(weight)

print("Chiều cao trung bình:", avg_height)
print("Cân nặng trung bình:", avg_weight)
print("Độ lệch chuẩn chiều cao:", std_height)
print("Độ lệch chuẩn cân nặng:", std_weight)