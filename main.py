#import libraries
import pandas as pd
from datetime import datetime

#read the csv file
df_csv = pd.read_csv('data/shipments.csv')

#count of shipment status
status_counts = df_csv['status'].value_counts()

#coverted from series to table
status_counts_reset = status_counts.reset_index()

#total freight cost calculation
total_fc = df_csv['freight_cost'].sum()

#converted the single number output to a DataFrame
df_fc = pd.DataFrame({
          'Metric' : ['Total Freight Cost'],
          'Value' : [total_fc]
        })

#converted the text dates to datetime objects
today = datetime.today()
converted_exp_del = pd.to_datetime(df_csv['expected_delivery'])

#filtered the overdue shipments
overdue = df_csv[(converted_exp_del<today) & (df_csv['status']!='Delivered')]

#excel file creation - full shipment data table
df_csv.to_excel("output/shipments.xlsx", index=False)

#excel file creation - summary of status count, total freight count and overdue list
with pd.ExcelWriter("output/summary.xlsx") as writer:
  status_counts_reset.to_excel(writer, startrow=0, index=False)
  overdue.to_excel(writer, startrow=7, index=False)
  df_fc.to_excel(writer, startrow=13, index=False)

