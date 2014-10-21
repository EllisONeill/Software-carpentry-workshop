import sys
import pandas as pd
import analyze_mosquito_lib as mosquito_lib


filename = sys.argv[1]

print "~"
print "~"
print "Analysing", filename
print "~"
print "~"

data=pd.read_csv(filename)
data["temperature"]=mosquito_lib.fahr_to_celsius(data["temperature"])
parameters=mosquito_lib.analyze(data,filename.replace("csv","png"))

parameters.to_csv(filename.replace("data", "parameters"))

print parameters

