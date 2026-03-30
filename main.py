import pandas as pd
from datetime import datetime

df_csv = pd.read_csv('data/shipments.csv')
print(df_csv)

status_counts = df_csv['status'].value_counts()
print(status_counts)
status_counts_reset = status_counts.reset_index()


total_fc = df_csv['freight_cost'].sum()
print(total_fc)
df_fc = pd.DataFrame({
          'Metric' : ['Total Freight Cost'],
          'Value' : [total_fc]
        })

today = datetime.today()
converted_exp_del = pd.to_datetime(df_csv['expected_delivery'])
overdue = df_csv[(converted_exp_del<today) & (df_csv['status']!='Delivered')]
print(overdue)

df_csv.to_excel("output/shipments.xlsx", index=False)

with pd.ExcelWriter("output/summary.xlsx") as writer:
  status_counts_reset.to_excel(writer, startrow=0, index=False)
  overdue.to_excel(writer, startrow=7, index=False)
  df_fc.to_excel(writer, startrow=13, index=False)

