'''
Homework8 Exercixe 1
Riley Fitzgibbons

Transpose an excel sheet and save it to another sheet
'''

import pandas as pd
import numpy as np

# Load File
fileName = 'EX1_test.xlsx'
book = pd.read_excel(fileName, header=None)

# Gather data and convert to normal array
array = pd.DataFrame(book.head())
array = array.values

# Transpose and put in dataframe
arrayT =[[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]
arrayT_w = pd.DataFrame(arrayT)


# Write to excel book in another sheet
writer = pd.ExcelWriter('trans_'+fileName)
arrayT_w.to_excel(writer,'Sheet2',index=False)
writer.save()