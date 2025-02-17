import pandas as pd

# Đọc file CSV
df = pd.read_csv('processed_dulieuxettuyendaihoc.csv')

# Sắp xếp điểm DH1 theo thứ tự tăng dần
df_sorted_dh1 = df.sort_values(by='DH1')
print(df_sorted_dh1[['DH1']].head())
