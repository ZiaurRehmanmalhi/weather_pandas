import pandas as pd


file_path = "f1.csv"
data_frame = pd.read_csv(file_path)

max_temperature = data_frame['Max TemperatureC']
min_temperature = data_frame['Min TemperatureC']
average = (max_temperature - min_temperature)/2 

print(average)
