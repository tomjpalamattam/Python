# First we import the module panda as pd
import pandas as pd
import re

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\PythonTest\extra\complete.xlsx')

#df.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries

EU_df=df.loc[df['Country Association'].str.contains('EU', na=False)] # this dataframe stores EU laws
EEA_df=df.loc[df['Country Association'].str.contains('EEA', na=False)] # this dataframe stores EEA laws
EU_EEA_exclusive_df=df.loc[~df['Country Association'].str.contains('EU', na=False) & df['Country Association'].str.contains('EEA', na=False)] # this dataframe stores EEA laws but not part of EU
EU_EEA_common_df=df.loc[df['Country Association'].str.contains('EU', na=False) & df['Country Association'].str.contains('EEA', na=False)] # this dataframe stores common laws between EEA and EU
Worldwide_df=df.loc[df['Country Association'].str.contains('Worldwide', na=False)] # this dataframe stores Worldwide laws

EU_EEA_common_df.reset_index(drop=True, inplace=True)
EU_EEA_exclusive_df.reset_index(drop=True, inplace=True)
EU_df.reset_index(drop=True, inplace=True)
EEA_df.reset_index(drop=True, inplace=True)


if len(EU_df.merge(EEA_df).drop_duplicates()) == len(EEA_df.drop_duplicates()):
    print("EEA is subset of EU")
else:
    print(" EEA Not a subset of EU, the diffrence is:",len(EEA_df.drop_duplicates()) -  len(EU_df.merge(EEA_df).drop_duplicates()))

print(len(EU_EEA_exclusive_df.index))    
print(len(EU_EEA_common_df.index))
print(len(EU_df.index))
print(len(EEA_df.index))


            
            
# For EU

df_sort=Worldwide_df # Here, type the dataframe to be sorted.

lst1=['India', 'Belgium', 'Belarus','Czechia'] #Applicable countries
lst2=[]
tmplst1=[]
tmplst2=[]
i=0

for cell in df_sort['Country']:
    i=i+1
    lst2=cell.split(',')
    for item in lst2:
        if str(item) in lst1:
            tmplst1.append(str(item))   # Appending country name to the list 'tmplst1'
            tmplst2.append(str(df_sort.iloc[i-1,0]))  # Appending ID to the list 'tmplst2'
dflst1=pd.DataFrame(tmplst1, columns = ['Country'])   
dflst2=pd.DataFrame(tmplst2, columns = ['ID']) 
frames = [dflst1, dflst2]
result_df = pd.concat(frames,axis=1)
result_df.sort_values(['Country'], ascending=True, inplace=True)

tempdf=result_df.drop_duplicates(subset=['ID'])
k=0
result_df.reset_index(drop=True, inplace=True)
tempdf.reset_index(drop=True, inplace=True)

print(tempdf['ID']) #print unique ID'S

for item1 in tempdf['ID']: # This dataframe 'tempdf' have column 'ID' without duplicates
    print('Checking for ID', item1)
    k=0
    for item2 in result_df['ID']: # This dataframe 'result_df' have column 'ID' with duplicates
        k=k+1
        if str(item1)==str(item2): # compares columns 'ID' between these two dataframes 'temp_df' and 'result_df' to print out countries sharing the same regulation ID. 
            print('Country:',result_df.iloc[k-1,0])
    
    