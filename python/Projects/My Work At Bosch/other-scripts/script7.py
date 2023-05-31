# First we import the module panda as pd
import pandas as pd
import re

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\PythonTest\extra\complete.xlsx')

df.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries

result_df1=df.loc[~df['Country'].str.contains(',', na=False)] # Removes raws where column 'Country' has a comma (when there is comma, there is more than one country)

mask=df['Country Association'].str.len() > 1 # If there is an entry in column 'Country Association'. The length of that element should be greater than '1'. mask stores a 'True' or 'False' value. 

result_df2 = df.loc[mask]  # A new dataframe 'result_df2' is created to remove the 'fasle' values.

result_df3=df.loc[df['Country Association'].str.len() == 1 & df['Country'].str.contains(',', na=False)] # To sort values with no entry in column 'Country association' (somehow, eventhough there is not a value in 'Country association', the length is '1' instead of zero) and has a comma in column 'Country'
result_df3.reset_index(drop=True, inplace=True)
lst1=['India', 'Belgium', 'Belarus','Czechia'] #Applicable countries
lst2=[]
tmplst1=[]
tmplst2=[]
i=0

for cell in result_df3['Country']:
    i=i+1
    lst2=cell.split(',')
    for item in lst2:
        if str(item) in lst1:
            tmplst1.append(str(item))   # Appending country name to the list 'tmplst1'
            tmplst2.append(str(result_df3.iloc[i-1,0]))  # Appending ID to the list 'tmplst2'. Doubt exist between 'i' or 'i-1'.
dflst1=pd.DataFrame(tmplst1, columns = ['Country'])   
dflst2=pd.DataFrame(tmplst2, columns = ['ID']) 
frames = [dflst1, dflst2]
result_df4 = pd.concat(frames,axis=1)
result_df4.sort_values(['Country'], ascending=True, inplace=True)

tempdf=result_df4.drop_duplicates(subset=['ID'])
k=0
result_df4.reset_index(drop=True, inplace=True)
tempdf.reset_index(drop=True, inplace=True)

print(tempdf['ID']) #print unique ID'S

for item1 in tempdf['ID']: # This dataframe 'tempdf' have column 'ID' without duplicates
    print('Checking for ID', item1)
    k=0
    for item2 in result_df4['ID']: # This dataframe 'result_df' have column 'ID' with duplicates
        k=k+1
        if str(item1)==str(item2): # compares columns 'ID' between these two dataframes 'temp_df' and 'result_df' to print out countries sharing the same regulation ID. 
            print('Country:',result_df4.iloc[k-1,0])
    
result_df1.to_excel('Countries.xlsx', index=False)
result_df2.to_excel('With_Coutry_Association.xlsx', index=False)
result_df3.to_excel('Countries_with_more_than_one_country.xlsx', index=False)
result_df4.to_excel('Countries_with_more_than_one_country-sorted.xlsx', index=False)