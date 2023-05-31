# First we import the module panda as pd
import pandas as pd
import re
import numpy as np


# Get unique 'Country Associations'

def Country_Association(df):
    
    list1=[]
    df_1=df.loc[~df['Country Association'].str.contains(',', na=False)] # Drops if multiple 'Country Association' (which will be comma seperated) exists
    df_1=df_1[df_1['Country Association'].str.len() > 1 ] 
    df_1.reset_index(drop=True, inplace=True)
    df_1.drop_duplicates(subset=['Country Association'], inplace=True)
    for item in df_1['Country Association']:
        list1.append(str(item))
    return list1

# Reset index
def reset_index(df_index):
    df_index.reset_index(drop=True, inplace=True)
    return df_index


class Countries:
    def __init__(self,list1,df):
        self.list1=list1
        self.df=df

#Get the 'Countries' for each first entry of unique 'Country Association' 

    def Countries_first_entry(self,char):
        print('Executing:',char)
        cf1=[]
        df_2=df.loc[~df['Country Association'].str.contains(',', na=False)] # Get rid of raws with multiple 'Country associations'
        df_2=df_2.loc[df_2['Country Association'].str.len() > 1] # Get rid of raws that has no 'Country Associations' 
        df_2.sort_values(['Country Association'], ascending=True, inplace=True) 
        df_2=reset_index(df_2)
        for item in list1:
            cf1.append(df['Country'].loc[df['Country Association'] == item][0:1]) # Gives the first entry of column 'Country' where country association is in list1 and then append it to the list 'cf'

        arr1=np.array(cf1) # create a np array 'arr1' from the list 'cf' 
        return arr1,df_2

#Get the 'Countries' for each largest entry of unique 'country association' 

    def Countries_largest_entry(self,char):
        print('Executing:',char)
        df_2=df.loc[~df['Country Association'].str.contains(',', na=False)] # Get rid of raws with multiple 'Country associations'
        df_2=df_2.loc[df_2['Country Association'].str.len() > 1] # Get rid of raws that has no 'Country Associations' 
        df_2.sort_values(['Country Association'], ascending=True, inplace=True) 
        df_2=reset_index(df_2)
        cf2=[]
        for item1 in list1:
            #print('looking for largest country section for country association:',item1)
            temp_df= df_2.loc[df_2['Country Association'] == item1] #creates a temporary dataframe of the same 'Country Association'
            k=temp_df['Country'].str.len().max() # prints maximum string length of column 'Country' for the given 'Country Association'
            cf2.append(temp_df['Country'].loc[temp_df['Country'].str.len() == k][0:1]) # the first entry for the maximum stringsize of column 'Country' for the given 'Country Association' is appended to the list cf2
        arr2=np.array(cf2)
        return arr2,df_2
            
            

#A diffrent way of diaplying array
#for item in range(len(arr1)):
#    print(arr1[item][0],'\n')
    
           

# For displaying the countries outside of the array 'arr1' (old 'for loop' - dont use)


#for item1 in arr1:
#    ok_items=0
#    not_ok_items=0
#    print('Checking:',item1,'\n' )
#    for item2 in df['Country']:
#        if(item1==item2):
#            #print('OK')
#            ok_items=ok_items+1
#        else:
#            #print('IDK man something wrong about dis:', item2) 
#            not_ok_items=not_ok_items+1
#            #print the regid and also which CA
            
#    print('for',item1,'OK:',ok_items,'Not_OK:',not_ok_items)

#arr2=np.empty # initialize empty np array 'arr2'
#arr2=np.array('df_2['Country']') # initialize np array 'arr2' with values of column 'Country' of databse 'df_2'
#arr2 == df_2['Country'].to_numpy() # np array 'arr2' Stores 'True' or 'False' values based on column 'Country' of databse 'df_2'
#arr2=df_2['Country'] #Gives np array values from a dataframe column 'Country' of the dataframe 'df_2'
#arr3=np.empty


# For displaying the countries outside of the array 'arr2'

def display(list1,df_2):
    iter=0
    for item1 in list1:
        ok_items=0
        not_ok_items=0
        iter=iter+1
        print('looking for match and not match for Country Association:',item1, 'and Country:', arr2[iter-1][0])
        temp_df= df_2.loc[df_2['Country Association'] == item1] #creates a temporary dataframe of the same 'Country Association'
        for item2 in temp_df['Country']:
            if arr2[iter-1][0]==item2:
                ok_items=ok_items+1
            else:
                not_ok_items=not_ok_items+1
        print('Match:',ok_items,'Not_Match:',not_ok_items)

    
    
# To print column 'Country' variation for the same 'Country Associations' 
def distribution(list1,df_2):    
    appended_data=[]
    for item1 in list1:
        print('\n checking for Country Association:',item1)
        temp_df= df_2.loc[df_2['Country Association'] == item1] #creates a temporary dataframe of the same 'Country Association'
        tt_df=temp_df['Country'].value_counts().to_frame() # prints column 'Country' variation for the respective 'Country Associations' in dataframe 'temp_df' 
        print(tt_df)    
    

    
#main    
df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Python\Docs\extra\Data_Quality\data.xlsx')    
print(len(df.loc[(df['Country Association'].str.len() > 1) & (~df['Country Association'].str.contains(',', na=False))])) # prints length of entries with single country associations
char1='Countries first entry'
char2='Countries largest entry'
list1=Country_Association(df)
temp=Countries(list1,df) # temp is of class countries
arr2,df2=temp.Countries_first_entry(char1)
#arr2,df2=temp.Countries_largest_entry(char2)
distribution(list1,df2)