# First we import the module panda as pd
import pandas as pd
import re
import numpy as np

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\PythonTest\extra\complete.xlsx')


result_df1=df.loc[~df['Country'].str.contains(',', na=False)] # Removes raws where column 'Country' has a comma (when there is comma, there is more than one country)

result_df2=df.loc[df['Country'].str.contains(',', na=False)] # dataframe consisting of more than one country

result_df1.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries

result_df1.reset_index(drop=True, inplace=True)
result_df2.reset_index(drop=True, inplace=True)

lst1=['India', 'Belgium', 'Belarus','Czechia'] #Applicable countries
lst2=[]
tmplst1=[]
tmplst2=[]
tmplst3=[]
i=0

for cell in result_df2['Country']: # iterates through every element of column 'country' of dataframe result_df2
    i=i+1
    lst2=cell.split(',')  # This element is split based on commas to get individual countries in each cell of column 'country' of dataframe result_df2
    for item in lst2:
        if str(item) in lst1: # checks if the countries match with 'applicable countries'
            if len(result_df2.iloc[i-1,5]) > 1:  # checks if country association exists
                tmplst1.append(str(item))   # Appending country name to the list 'tmplst1'
                tmplst2.append(str(result_df2.iloc[i-1,0]))  # Appending ID to the list 'tmplst2'
                tmplst3.append(str(result_df2.iloc[i-1,5]))  # Appending 'Country association' to the list 'tmplst3'
            else:
                tmplst1.append(str(item))   # Appending country name to the list 'tmplst1'
                tmplst2.append(str(result_df2.iloc[i-1,0]))  # Appending ID to the list 'tmplst2'
                tmplst3.append('Nothing Here Buddy')  # Appending 'Country association' to the list 'tmplst3'
    
dflst1=pd.DataFrame(tmplst1, columns = ['Country'])   
dflst2=pd.DataFrame(tmplst2, columns = ['ID']) 
dflst3=pd.DataFrame(tmplst3, columns = ['Country Association']) 
frames = [dflst1, dflst2, dflst3]
result_df3 = pd.concat(frames,axis=1)
result_df3.sort_values(['Country'], ascending=True, inplace=True)

tempdf=result_df3.drop_duplicates(subset=['ID']) # To get a dataframe 'tempdf' with unique ID
k=0
country_assoc_counter=0
result_df3.reset_index(drop=True, inplace=True)
tempdf.reset_index(drop=True, inplace=True)
print(tempdf['ID']) #print unique ID'S

for item1 in tempdf['ID']: # This dataframe 'tempdf' have column 'ID' without duplicates
    k=0
    country_assoc_counter=country_assoc_counter+1
    print('Checking for ID', item1, 'with Country Association:', tempdf.iloc[country_assoc_counter-1,2])
    for item2 in result_df3['ID']: # This dataframe 'result_df' have column 'ID' with duplicates
        k=k+1
        if str(item1)==str(item2): # compares columns 'ID' between these two dataframes 'temp_df' and 'result_df' to print out countries sharing the same regulation ID. 
            print('Country:',result_df3.iloc[k-1,0])
    
result_df1.to_excel('Countries.xlsx', index=False)
result_df2.to_excel('Other_Than_Single_Countries.xlsx', index=False)
result_df3.to_excel('Other_Than_Single_Countries_Sorted.xlsx', index=False)



# for colleagues
country_var='India' # define the country the college is assigned in
comm_count_var=0
y=0
for item in result_df3['Country']: # This loops through the column 'Country' in dataframe 'result_df3'
    y=y+1
    comm_count_var=0
    if str(item)==str(country_var): # checks if the countries in the dataframe 'result_df3' is the same as that of the collegeue specified country
        print('ID:',result_df3.iloc[y-1,1],'Country association:',result_df3.iloc[y-1,2]) # prints the regulation ID relevant for the specified country for the colleague
        temp_var=str(result_df3.iloc[y-1,1])
        for item_var in result_df3['ID']: # This loops through the column 'ID' in dataframe 'result_df3'
            comm_count_var= comm_count_var +1
            if item_var == temp_var: # checks if the relevant 'ID' is shared by another country
                print('countries sharing this ID', result_df3.iloc[comm_count_var-1,0])
                
                
                
                
# for finding laws common to every country in list 'lst1'


contains = [df['Country'].str.contains(i) for i in lst1]
result_common_countries = df[np.all(contains, axis=0)]

result_common_countries.to_excel('Laws_Common_to_all_Countries.xlsx', index=False)


