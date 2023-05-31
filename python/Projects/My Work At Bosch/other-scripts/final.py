# First we import the module panda as pd

import pandas as pd
import re
import numpy as np



# Reset index
def reset_index(df_index_dropped):
    df_index_dropped.reset_index(drop=True, inplace=True)
    return df_index_dropped



def dataframes(df):
    df_single_country=df.loc[~df['Country'].str.contains(',', na=False)] # Removes raws where column 'Country' has a comma (when there is comma, there is more than one country)
    df_single_country.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries
    df_more_than_one_country=df.loc[df['Country'].str.contains(',', na=False)] # dataframe consisting of more than one country
    df_single_country=reset_index(df_single_country)
    df_more_than_one_country=reset_index(df_more_than_one_country)
    return df_single_country,df_more_than_one_country


def df_more_than_one_country_sorted_method1(df_more_than_one_country,lst1): # old method
    
    i=0
    lst2=[]
    tmplst1=[]
    tmplst2=[]
    tmplst3=[]
    for cell in df_more_than_one_country['Country']: # iterates through every element of column 'country' of dataframe df_more_than_one_country
        i=i+1
        lst2=cell.split(',')  # This element is split based on commas to get individual countries in each cell of column 'country' of dataframe df_more_than_one_country
        for item in lst2:
            if str(item) in lst1: # checks if the countries match with 'applicable countries'
                if len(df_more_than_one_country.iloc[i-1,5]) > 1:  # checks if country association exists
                    tmplst1.append(str(item))   # Appending country name to the list 'tmplst1'
                    tmplst2.append(str(df_more_than_one_country.iloc[i-1,0]))  # Appending ID to the list 'tmplst2'
                    tmplst3.append(str(df_more_than_one_country.iloc[i-1,5]))  # Appending 'Country association' to the list 'tmplst3'
                else:
                    tmplst1.append(str(item))   # Appending country name to the list 'tmplst1'
                    tmplst2.append(str(df_more_than_one_country.iloc[i-1,0]))  # Appending ID to the list 'tmplst2'
                    tmplst3.append('Nothing Here Buddy')  # Appending 'Country association' to the list 'tmplst3'
    
    dflst1=pd.DataFrame(tmplst1, columns = ['Country'])   
    dflst2=pd.DataFrame(tmplst2, columns = ['ID']) 
    dflst3=pd.DataFrame(tmplst3, columns = ['Country Association']) 
    frames = [dflst1, dflst2, dflst3]
    df_more_than_one_country_sorted = pd.concat(frames,axis=1)
    df_more_than_one_country_sorted.sort_values(['Country'], ascending=True, inplace=True)
    return df_more_than_one_country_sorted


def df_more_than_one_country_sorted_method2(df_more_than_one_country,lst1): # new method

    appended_data = []
    for item in lst1: # iterates through every country in lst1
        #print(df_more_than_one_country['Country'].str.contains(item, case=False, na=None)) # print True or False
        #print('checking for country:',item,' output \n' ,df_more_than_one_country['Country'].loc[df_more_than_one_country['Country'].str.contains(item, case=False, na=None)]) 
        df_more_than_one_country.loc[df_more_than_one_country['Country'].str.contains(item, case=False, na=None), 'Checked For Country'] = item # This line checks the column 'Country' in dataframe 'df_more_than_one_country' actually has any country in list 'lst1'. if the condition is statisfied i.e True, a new column 'Checked For Country' is made with value of the country (variable 'item' ) 
        appended_data.append(df_more_than_one_country.loc[df_more_than_one_country['Country'].str.contains(item, case=False, na=None)])   
    appended_df = pd.concat(appended_data)
    appended_df = reset_index(appended_df)
    return appended_df
    # 'df_more_than_one_country['Country'].loc[df_more_than_one_country['Country'].str.contains(item, case=False, na=None)]'  is of the form df['Column'].loc['Condition']  
    # where condition is either 'True' or 'False'. Condition is 'df_more_than_one_country['Country'].str.contains(item, case=False, na=None)' gives either 'True' or 'False' if the column 'Country' contains the string in list 'lst1' 
    
    
class utilities:
    def __init__(self,lst1):
        self.list1=lst1
        
        
    def shared_id(self,df_more_than_one_country_sorted):
        df=df_more_than_one_country_sorted
        tempdf=df.drop_duplicates(subset=['ID'])
        print('unique IDS are',tempdf['ID'])
        df.reset_index(drop=True, inplace=True)
        tempdf.reset_index(drop=True, inplace=True)
        for item in tempdf['ID']: # This dataframe 'tempdf' have column 'ID' without duplicates
            print('checking for ID:',item,'\n',df['Checked For Country'].loc[df['ID'] == item])
            
            
            
    def shared_id_between_country(self,country,df_more_than_one_country_sorted):
        df=df_more_than_one_country_sorted
        temp_df= df.loc[df['Checked For Country'] == country] # this dataframe 'temp_df' stores the values of dataframe 'df' when the value of column 'Checked For Country' in 'df' is 'india'
        for item in temp_df['ID']:
            print('The ID', item, 'is shared by countries \n', df['Checked For Country'].loc[df['ID'] == item])
            
            
# for finding laws common to every country in list 'lst1'

    def common_regs(self, df):
        contains = [df['Country'].str.contains(i) for i in lst1]   #The for loop at end actually can be used if its a list. thats why we use '[' and ']'
        common_regs_df = df[np.all(contains, axis=0)]
        common_regs_df=reset_index(common_regs_df)
        return common_regs_df
    


            
#main


df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Python\Docs\extra\complete.xlsx')

df_single_country,df_more_than_one_country = dataframes(df)
lst1=['India', 'Belgium', 'Belarus','Czechia'] #Applicable countries
df_more_than_one_country_sorted = df_more_than_one_country_sorted_method2(df_more_than_one_country,lst1)
temp=utilities(lst1) # temp is of class countries
temp.shared_id(df_more_than_one_country_sorted)
#temp.shared_id_between_country('India',df_more_than_one_country_sorted)
common_regs_df=temp.common_regs(df)
#common_regs_df['ID']




