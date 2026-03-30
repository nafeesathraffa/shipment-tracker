import pandas as pd
from datetime import datetime

df_csv = pd.read_csv('data/shipments.csv')
print(df_csv)

status_counts = df_csv['status'].value_counts()
print(status_counts)

total_fc = df_csv['freight_cost'].sum()
print(total_fc)

today = datetime.today()
converted_exp_del = pd.to_datetime(df_csv['expected_delivery'])
overdue = df_csv[(converted_exp_del<today) & (df_csv['status']!='Delivered')]
print(overdue)
