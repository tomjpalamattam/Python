# First we import the module panda as pd
import pandas as pd



# To read the excel file

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\PythonTest\extra\complete.xlsx')
#print(df.columns)
df.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries
i=0
k=0
lst1 = [] # Initialising a list 'lst1'
lst2 = [] # Initialising a list 'lst2'
for cell in df['Country']:       # loops through each element of the column "column_toc". df["column"] provides each element of the column
    i=i+1
#    if len(str(cell)) <= 12:      # if the cell has more than one country, it will have more than 12 characters
    if "," not in str(cell):      # if the cell has more than one country, it will be commas seperated
        k=k+1
        #print(k,'.',df.iloc[i,0],'Country:',cell)     # To Print regulations ID, which is in column 1
        lst1.append(str(df.iloc[i,0]))   # Append the values of 'ID' to the list 'lst1'
        lst2.append(str(cell))   # Append the values of 'Country' to the list 'lst2' 

#df.loc[df['Country'].str.contains(',', na=False)] #list non-national laws (They all have comma seperated countries)
#df.loc[~df['Country'].str.contains(',', na=False)] #list national laws (They so not have commas)



#for item in range(len(lst1)):     # For loop for displaying list 'lst'
#    print(item+1, '.', lst1[item])

df1=pd.DataFrame(lst1)   
df2=pd.DataFrame(lst2)  
frames = [df1, df2]
result_df = pd.concat(frames,axis=1) # Joins together two dataframes. To export to single column use 'axis=0'
result_df.to_excel('Modified.xlsx', index=False) # export to excel