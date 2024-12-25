import numpy as np
import pandas as pd

# Đọc dữ liệu từ file
positions = pd.read_csv('positions.txt', header=None, names=['position'])
heights = pd.read_csv('heights.txt', header=None, names=['height'])

# Kết hợp hai DataFrame
data = pd.concat([positions, heights], axis=1)

# Tính chiều cao trung bình của các thủ môn (GK)
avg_height_gk = data[data['position'] == 'GK']['height'].mean()
print("Chiều cao trung bình của thủ môn:", avg_height_gk)

# Tính chiều cao trung bình của các vị trí khác
avg_height_others = data[data['position'] != 'GK']['height'].mean()
print("Chiều cao trung bình của các vị trí khác:", avg_height_others)

# Sắp xếp dữ liệu theo chiều cao giảm dần và lấy 5 cầu thủ cao nhất
top_5_tallest = data.sort_values('height', ascending=False).head(5)
print("5 cầu thủ cao nhất:")
print(top_5_tallest)