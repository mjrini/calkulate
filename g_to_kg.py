
import pandas as pd

data = pd.read_excel("metadata1.xlsx")
data.to_excel("metadata1.xlsx",index=False)
data["analyte_mass g"] = (data["analyte_mass g"]/1000)
print(data["analyte_mass g"])


data["file name"] = data["file name"]+".txt"
print(data["file name"])