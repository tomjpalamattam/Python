# First we import the module panda as pd
import pandas as pd



# To read the excel file

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\case14\case14.xlsx')
#print(df.columns)
df.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries
i=0
for cell in df['Country']:       # loops through each element of the column "column_toc". df["column"] provides each element of the column
    i=i+1
#    if len(str(cell)) <= 12:      # if the cell has more than one country, it will have more than 12 characters
    if "," not in str(cell):      # if the cell has more than one country, it will be commas seperated
       print(df.iloc[i-1,0],'Country:',cell)     # To Print regulations ID, which is in column 1

#df.loc[df['Country'].str.contains(',', na=False)] #list non-national laws (They all have comma seperated countries)
#df.loc[~df['Country'].str.contains(',', na=False)] #list national laws (They so not have commas)
#result_df=df.loc[~df['Country Association'].str.contains(',', na=False) & ~df['Country Association'].str.contains('UNECE', na=False)] # multiple conditions