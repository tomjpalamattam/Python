# First we import the module panda as pd
import pandas as pd



# To read the excel file without na values

#df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\C2P+NORMASTER+GUIDANCE+STANDARDS\NationalLaws-automatic-Normmaster+C2P.xlsx', keep_default_na=False)


# To read the excel file

df1 = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\To_Test\exported_MSExcelX_66616_20230322_141509_1.xlsx',  usecols = [0]) # reads only first column and stores to datafarame 'df1'
df2 = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\To_Test\exported_MSExcelX_66616_20230322_141600_2.xlsx',  usecols = [0]) # reads only first column and stores to datafarame 'df2'
df1.rename(columns={'ID': 'Country1'}, inplace=True)  # Change column name from 'ID' to 'Country 1'
df2.rename(columns={'ID': 'Country2'}, inplace=True) # Change column name from 'ID' to 'Country 2'
frames = [df1, df2] # A new dataframe 'frames'
result_df = pd.concat(frames,axis=1) # Joins together two dataframes To export to single column use 'axis=0'
#result_df = result_df.rename(columns={'ID': 'newName1', 'ID': 'newName2'}) # To change column names from 'ID' to desired name
result_df.to_excel('Modified.xlsx', index=False) # export to excel


