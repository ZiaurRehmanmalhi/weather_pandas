import pandas as pd


file_path = "f2.csv"
data_frame = pd.read_csv(file_path)

event_list = data_frame[' Events']

rain_dates = data_frame[event_list.isin(['Rain', 'Snow', 'Rain-Snow'])]
pr
print(rain_dates['PKT'])
