# Import packages
import openpyxl as xl
import pandas as pd
import os

for file in os.listdir('.'):
	# Skip non-xlsx files, load the workbook object.
	if file.endswith('.xlsx'):
		temp = xl.load_workbook(file)
		numSheets = len(temp.get_sheet_names())
		# For every sheet
		for i in range(0,numSheets):
			pd_temp = pd.read_excel(file, sheetname=i)
			pd_temp.to_csv(str(i)+file+'.csv', sep=',')