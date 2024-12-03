import pandas as pd


file = pd.read_excel("Test.xlsx")
file = file.sort_values(by='Number')
file['SQ_Number'] = file.Number ** 2
print(file.describe())

file.to_excel("result.xlsx")
