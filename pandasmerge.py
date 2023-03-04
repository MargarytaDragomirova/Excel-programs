import pandas as pd
import os
import numpy as np

input_loc  = "/Users/margarita/Desktop/exel_dosyalar/"
output_loc = "/Users/margarita/Desktop/exel_dosyalar/"

fileList = os.listdir(input_loc)

df1 = []
for files in fileList:
     if files.endswith("_Structured.xlsx"):
        df2 = pd.read_excel(input_loc + files, skiprows=1)
        df2.index = [os.path.split(files)] * len(df2)
        df1.append(df2)

df1 = pd.concat(df1)


df1.to_excel(output_loc + "finalStructured.xlsx")