import numpy as np

# Tạo mảng nhiệt độ ngẫu nhiên (30 ngày), giá trị từ 15 đến 35 độ C
np.random.seed(42)  # Đảm bảo tính tái lập
temperatures = np.round(np.random.uniform(15, 35, size=30), 2)

# Tính nhiệt độ trung bình trong tháng
average_temp = np.mean(temperatures)

print("Nhiệt độ hàng ngày:", temperatures)
print("Nhiệt độ trung bình:", round(average_temp, 2))

# Xác định ngày có nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
max_temp_day = np.argmax(temperatures) + 1
min_temp_day = np.argmin(temperatures) + 1

# Tính sự chênh lệch nhiệt độ giữa các ngày
daily_diff = np.abs(np.diff(temperatures))
max_diff = np.max(daily_diff)
max_diff_day = np.argmax(daily_diff) + 1  # Vì tính từ ngày đầu tiên đến ngày thứ hai

print("Ngày nhiệt độ cao nhất: Ngày", max_temp_day, "với", max_temp, "độ C")
print("Ngày nhiệt độ thấp nhất: Ngày", min_temp_day, "với", min_temp, "độ C")
print("Ngày có sự chênh lệch nhiệt độ lớn nhất:", max_diff_day, "với chênh lệch", round(max_diff, 2), "độ C")

# Tất cả các ngày có nhiệt độ cao hơn 20 độ C
days_above_20 = np.where(temperatures > 20)[0] + 1
temps_above_20 = temperatures[temperatures > 20]

# Lấy nhiệt độ của ngày 5, 10, 15, 20, và 25
specific_days = [5, 10, 15, 20, 25]
specific_temps = temperatures[np.array(specific_days) - 1]

# Tìm nhiệt độ của các ngày có nhiệt độ trên trung bình
above_avg_days = np.where(temperatures > average_temp)[0] + 1
above_avg_temps = temperatures[temperatures > average_temp]

# Lấy nhiệt độ của các ngày chẵn/lẻ trong tháng
even_days = temperatures[1::2]  # Ngày chẵn (index 1, 3, ...)
odd_days = temperatures[0::2]   # Ngày lẻ (index 0, 2, ...)

print("Ngày có nhiệt độ > 20°C:", days_above_20)
print("Nhiệt độ các ngày > 20°C:", temps_above_20)
print("Nhiệt độ của các ngày 5, 10, 15, 20, 25:", specific_temps)
print("Ngày có nhiệt độ trên trung bình:", above_avg_days)
print("Nhiệt độ của các ngày chẵn:", even_days)
print("Nhiệt độ của các ngày lẻ:", odd_days)