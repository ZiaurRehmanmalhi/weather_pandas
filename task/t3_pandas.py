import pandas as pd


file_path = "f2.csv"
data_frame = pd.read_csv(file_path)

event_list = data_frame[' Events']
event_dates_bol = data_frame[event_list.isin(['Rain', 'Snow', 'Rain-Snow'])]
event_dates = event_dates_bol['PKT']

print(event_dates)
