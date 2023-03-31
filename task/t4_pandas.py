import pandas as pd


file_path = "f2.csv"
data_frame = pd.read_csv(file_path)

event_list = data_frame[' Events']
data_thunderstorm = data_frame[event_list.isin(['Thunderstorm'])]
date = pd.to_datetime(data_thunderstorm['PKT'])
week_days = date.dt.strftime('%A')

print(week_days)

