import pandas as pd

# Đọc dữ liệu từ tập tin drinks.csv với index_col là cột đầu tiên của dữ liệu
drink = pd.read_csv(r'C:\Users\Dungggxg\Documents\GitHub\PythonAdvanced\BTVNC4\drinks.csv', index_col=0)

# Kiểu dữ liệu và kích thước của drink
print(f"Kiểu dữ liệu của drink: {type(drink)}")
print(f"Kích thước của drink: {drink.shape}")

# Hiển thị tên các cột của drink
print(f"Tên các cột của drink: {drink.columns.tolist()}")

# Xem 5 dòng dữ liệu đầu tiên và cuối cùng của drink
print("5 dòng dữ liệu đầu tiên của drink:")
print(drink.head())
print("\n5 dòng dữ liệu cuối cùng của drink:")
print(drink.tail())

# Số lượng bia tiêu thụ trung bình ở mỗi châu lục
avg_beer_per_continent = drink.groupby('continent')['beer_servings'].mean()
print("\nSố lượng bia tiêu thụ trung bình ở mỗi châu lục:")
print(avg_beer_per_continent)

# Thông tin thống kê tổng quát số lượng rượu vang được tiêu thụ ở mỗi châu lục
wine_stats_per_continent = drink.groupby('continent')['wine_servings'].describe()
print("\nThông tin thống kê tổng quát số lượng rượu vang được tiêu thụ ở mỗi châu lục:")
print(wine_stats_per_continent)

# Số lượng các loại bia và rượu tiêu thụ trung bình ở mỗi châu lục
avg_beer_wine_per_continent = drink.groupby('continent')[['beer_servings', 'wine_servings']].mean()
print("\nSố lượng các loại bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
print(avg_beer_wine_per_continent)

# Giá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục
median_beer_wine_per_continent = drink.groupby('continent')[['beer_servings', 'wine_servings']].median()
print("\nGiá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục:")
print(median_beer_wine_per_continent)

# Số lượng rượu mạnh tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục
spirit_stats_per_continent = drink.groupby('continent')['spirit_servings'].agg(['mean', 'max', 'min'])
print("\nSố lượng rượu mạnh tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục:")
print(spirit_stats_per_continent)

# Sắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ
sorted_drink = drink.sort_values(by='beer_servings')
print("\nSắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ:")
print(sorted_drink)

# 5 quốc gia có lượng tiêu thụ bia nhiều nhất
top_5_beer_countries = drink.nlargest(5, 'beer_servings')
print("\n5 quốc gia có lượng tiêu thụ bia nhiều nhất:")
print(top_5_beer_countries)

# 5 quốc gia có lượng tiêu thụ bia ít nhất
bottom_5_beer_countries = drink.nsmallest(5, 'beer_servings')
print("\n5 quốc gia có lượng tiêu thụ bia ít nhất:")
print(bottom_5_beer_countries)

# Chia các phần hiển thị kết quả trong terminal
print("\n" + "="*50 + "\n")

# Số lượng bia tiêu thụ trung bình ở mỗi châu lục
print("\nSố lượng bia tiêu thụ trung bình ở mỗi châu lục:")
print(avg_beer_per_continent)
print("\n" + "="*50 + "\n")

# Thông tin thống kê tổng quát số lượng rượu vang được tiêu thụ ở mỗi châu lục
print("\nThông tin thống kê tổng quát số lượng rượu vang được tiêu thụ ở mỗi châu lục:")
print(wine_stats_per_continent)
print("\n" + "="*50 + "\n")

# Số lượng các loại bia và rượu tiêu thụ trung bình ở mỗi châu lục
print("\nSố lượng các loại bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
print(avg_beer_wine_per_continent)
print("\n" + "="*50 + "\n")

# Giá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục
print("\nGiá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục:")
print(median_beer_wine_per_continent)
print("\n" + "="*50 + "\n")

# Số lượng rượu mạnh tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục
print("\nSố lượng rượu mạnh tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục:")
print(spirit_stats_per_continent)
print("\n" + "="*50 + "\n")

# Sắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ
print("\nSắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ:")
print(sorted_drink)
print("\n" + "="*50 + "\n")

# 5 quốc gia có lượng tiêu thụ bia nhiều nhất
print("\n5 quốc gia có lượng tiêu thụ bia nhiều nhất:")
print(top_5_beer_countries)
print("\n" + "="*50 + "\n")

# 5 quốc gia có lượng tiêu thụ bia ít nhất
print("\n5 quốc gia có lượng tiêu thụ bia ít nhất:")
print(bottom_5_beer_countries)
print("\n" + "="*50 + "\n")