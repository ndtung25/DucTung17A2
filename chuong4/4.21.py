import pandas as pd

# Đọc dữ liệu từ file euro12.csv
euro12 = pd.read_csv(r'C:\Users\Dungggxg\Documents\GitHub\PythonAdvanced\BTVNC4\euro2012.csv')

# In type, shape, danh sách các cột
print(type(euro12))
print(euro12.shape)
print(euro12.columns.tolist())

# In giá trị cột Goals
print(euro12['Goals'])

# Có bao nhiêu đội tham gia Euro2012?
print(euro12['Team'].nunique())

# In thông tin của Euro2012
print(euro12.info())

# Tạo data frame mới từ euro12 có tên là discipline chỉ chứa 3 cột Team, Yellow Cards, Red Cards
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# Sắp xếp discipline giảm dần theo 2 cột Red Cards, Yellow Cards
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print(discipline_sorted)

# a) Tính trung bình Yellow Cards
print(discipline['Yellow Cards'].mean())

# b) Lọc các đội đã ghi hơn 6 bàn thắng
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]
print(teams_more_than_6_goals)

# In các đội mà tên bắt đầu bằng 'G'
teams_start_with_G = euro12[euro12['Team'].str.startswith('G')]
print(teams_start_with_G)

# In 7 cột đầu của euro12
print(euro12.iloc[:, :7])

# In tất cả các cột, trừ 3 cột cuối
print(euro12.iloc[:, :-3])

# In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
print(euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# In các cột chỉ hiển thị Team, Shooting Accuracy từ England, Italy, Russia
print(euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']])