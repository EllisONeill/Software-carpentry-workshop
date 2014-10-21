import pandas as pd
import analyze_mosquito_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

data=pd.read_csv(filename)
data["temperature"]=mosquito_lib.fahr_to_celsius(data["temperature"])

print data.head()

