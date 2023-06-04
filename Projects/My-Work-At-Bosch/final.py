import pandas as pd
import glob
import numpy as np
import random

# User Input

path_input=r'C:\\Users\\JOT1WE\\Desktop\\Python\\Input' # Edit me - input folder
path_output=r'C:\\Users\\JOT1WE\\Desktop\\Python\\Output'  # Edit me - output folder
lst1=['Austria', 'Switzerland', 'Czechia','denmark', 'Germany', 'Spain', 'Croatia', 'Norway', 'Poland', 'Slovakia', 'Sierra leone']  # Edit me - Applicable Countries


# Algorithm

path_divided_market_specialists = os.path.join(path_output, "Market_Specialists_Divided")
path_not_divided_market_specialists = os.path.join(path_output, "Market_Specialists_Not_divided")
path_engineers = os.path.join(path_output, "Engineers")
os.mkdir(path_divided_market_specialists)
os.mkdir(path_engineers)
os.mkdir(path_not_divided_market_specialists)


def combine():
    name=[]
    dflist1=[]
    dflist2=[]
    for filename in glob.glob(str(path_input)+'\\features\\*.xlsx'): 
        temp_df = pd.read_excel(filename)
        name=str(filename).split('\\')
        name=name[-1]
        name=name.split('.')
        name=name[-2]
        temp_df['Extra']=np.nan
        temp_df['Extra'] = temp_df['Extra'].apply(lambda x: str(x)+', feature:'+str(name)) # we are appending the 'subcategory' name to the column 'Extra' because if not, if column 'Extra' has any 'SubCategory', it might gets overwritten
        dflist1.append(temp_df)
    df_feature=pd.concat(dflist1)

    for filename in glob.glob(str(path_input)+'\\subcategories\\*.xlsx'): 
        temp_df = pd.read_excel(filename)
        name=str(filename).split('\\')
        name=name[-1]
        name=name.split('.')
        name=name[-2]
        temp_df['Extra']= np.nan
        temp_df['Extra'] = temp_df['Extra'].apply(lambda x: str(x)+', Productcategory&Subcategory:'+str(name)) # we are appending the 'feature' name to the column 'Extra' because if not, if column 'Extra' has any 'Feature', it might gets overwritten
        dflist2.append(temp_df)
    
    df_subcat=pd.concat(dflist2)
    
    # combining rows by keeping all column same but column 'Extra' where its combined by comma
    df_subcat = df_subcat.groupby(['ID', 'Revision ID', 'Name', 'Regulation Title (EN)', 'Reference Number', 'Country Association', 'Country', 'Enforcement Status', 'Duplicate Process Status'], dropna=False)['Extra'].apply(', '.join).reset_index()
    df_feature = df_feature.groupby(['ID', 'Revision ID', 'Name', 'Regulation Title (EN)', 'Reference Number', 'Country Association', 'Country', 'Enforcement Status', 'Duplicate Process Status'], dropna=False)['Extra'].apply(', '.join).reset_index()
    
    frames = [df_feature, df_subcat]
    df=pd.concat(frames)
    
     # combining rows by keeping all column same but column 'Extra' where its combined by comma
    df = df.groupby(['ID', 'Revision ID', 'Name', 'Regulation Title (EN)', 'Reference Number', 'Country Association', 'Country', 'Enforcement Status', 'Duplicate Process Status'], dropna=False)['Extra'].apply(', '.join).reset_index()
    
    # removing 'nan'
    df['Extra'] = df['Extra'].str.replace('nan,', '')
    return df



# Reset index
def reset_index(df_index_dropped):
    df_index_dropped.reset_index(drop=True, inplace=True)
    return df_index_dropped



def dataframes(df):
    df_national_laws=df.loc[~df['Country'].str.contains(',', na=False)] # Removes raws where column 'Country' has a comma (when there is comma, there is more than one country)
    df_national_laws.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries
    df_shared_laws=df.loc[df['Country'].str.contains(',', na=False)] # dataframe consisting of more than one country
    df_national_laws=reset_index(df_national_laws)
    df_shared_laws=reset_index(df_shared_laws)

    return df_national_laws,df_shared_laws


def df_shared_laws_sorted(df_shared_laws,lst1): # new method

    appended_data = []
    for item in lst1: # iterates through every country in lst1
        df_shared_laws.loc[df_shared_laws['Country'].str.contains(item, case=False, na=None), 'Checked For Country'] = item # This line checks the column 'Country' in dataframe 'df_more_than_one_country' actually has any country in list 'lst1' and add a new column 'Checked for Country' if the situation is statisfied with the country it matched with.
        appended_data.append(df_shared_laws.loc[df_shared_laws['Country'].str.contains(item, case=False, na=None)])   
    appended_df = pd.concat(appended_data)
    appended_df = reset_index(appended_df)
    return appended_df


# This function returns a list of all unique country associations without CEN, CENELEC, EU and EEA
def Country_Association_all(df):
    
    CA_list=[]
    #df_shared_laws=df_shared_laws.loc[~df_shared_laws['Country Association'].str.contains(',', na=False)] # Drops if multiple 'Country Association' (which will be comma seperated) exists
    df=df[df['Country Association'].str.len() > 1 ] 
    df.reset_index(drop=True, inplace=True)
    df.drop_duplicates(subset=['Country Association'], inplace=True)
    for item in df['Country Association']:
        CA_list.append(str(item)) 
    Country_Association_list=[]
    for item in CA_list:
        item=item.split(",")
        Country_Association_list.extend(item)
    Country_Association_list=list(set(Country_Association_list))  # drops duplicates from the list
    Country_Association_list.remove('European Economic Area - EEA')
    Country_Association_list.remove('European Union (EU)')
    Country_Association_list.remove('CEN')
    Country_Association_list.remove('CENELEC')
    return Country_Association_list

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
            
            
            
    def shared_id_between_country(self,country,df_more_than_one_country_sorted,df_full):
        df=df_more_than_one_country_sorted
        temp_df= df.loc[df['Checked For Country'] == country] # this dataframe 'temp_df' stores the values of dataframe 'df' when the value of column 'Checked For Country' in 'df' is 'india'
        for item in temp_df['ID']:
            print('\n')
            print('The ID', item)
            print('The Features and subcategories are \n', df_full['Extra'].loc[df_full['ID'] == item])
            print('The name \n', df_full['Regulation Title (EN)'].loc[df_full['ID'] == item])
            print('Is shared by countries \n',df['Checked For Country'].loc[df['ID'] == item])
            
            
# for finding laws common to every country in list 'lst1'

    def common_regs(self, df):
        contains = [df['Country'].str.contains(i, case=False) for i in lst1]   #The for loop at end actually can be used if its a list. thats why we use '[' and ']'
        common_regs_df = df[np.all(contains, axis=0)]
        common_regs_df=reset_index(common_regs_df)
        return common_regs_df
    



    def market_specialists_engineers(self, df_complete,df,lst1,df_national_laws):
        temp_df_list=[]
        
        # For market specialists 'where shared regulations with no country associations are not divided randomly'
        for item in lst1:
            #print('output for loop',df_complete.loc[(~df_complete['Country Association'].str.len() > 1) & (df_complete['Shared Countries'].str.contains(item, na=False)) ]) # why doesnt this work?
            temp_df=df_complete.loc[~(df_complete['Country Association'].str.len() > 1) & (df_complete['Shared Countries'].str.contains(item, na=False)) ]
            temp_df_national_laws=df_national_laws.loc[(df_national_laws['Country'].str.contains(item, na=False)) | (df_national_laws['Country']==item)]
            temp_df_list = [temp_df, temp_df_national_laws]
            temp_df=pd.concat(temp_df_list)            
            temp_df.to_excel(str(path_not_divided_market_specialists)+'\\Country_'+ str(item) + '.xlsx', index=False)
        


        # For market specialists 'where shared regulations with no country associations are divided randomly among countries'
        rand_list=[]
        df_complete_temp=df_complete.loc[~(df_complete['Country Association'].str.len() > 1)]
        for index, row in df_complete_temp.iterrows(): 
            K=row[-1].split(',') # 'row' is an array which stores the entire row of the dataframe. row[-1] gives the last elemnt of that array which corresponds to element of column 'Shared Countries'. Then we split it based on commas and this value is stored in a new varaiable 'K'
            i=len(K)
            rand_list.append(K[random.randint(0,i-1)]) # a new list 'rand_list' is used to store random value of variable 'K', whose range is between 0 and maximum length of K
 
        df_complete_temp['Target Country']= rand_list    
        for item in lst1:
            temp_df=df_complete_temp.loc[~(df_complete_temp['Country Association'].str.len() > 1) & (df_complete_temp['Target Country'].str.contains(item, na=False)) ]
            temp_df_national_laws=df_national_laws.loc[(df_national_laws['Country'].str.contains(item, na=False)) | (df_national_laws['Country']==item)]
            temp_df_list = [temp_df, temp_df_national_laws]
            temp_df=pd.concat(temp_df_list)            
            temp_df.to_excel(str(path_divided_market_specialists)+'\\Country_'+str(item)+'.xlsx', index=False)        

        
        # For complete list of regulations
        
        df_complete.to_excel(str(path_output)+'\\complete_shared.xlsx', index=False)
    
    
        # For Engineers
        
        Country_Association_list=Country_Association_all(df)
        for item in Country_Association_list:
            temp_df=df_complete.loc[(df_complete['Country Association']==item) | (df_complete['Country Association'].str.contains(item, case=False, na=None))]
            temp_df.to_excel(str(path_engineers)+'\\CountryAssociation_'+str(item)+'.xlsx', index=False)  
        
        CA_EU_EEA_df=df_complete.loc[df_complete['Country Association'].str.contains('EU|EEA', case=False, na=None)]
        CA_CEN_CENELEC_df=df_complete.loc[(df_complete['Country Association'].str.contains('CEN|CENELEC', case=False, na=None))  | (df_complete['Country Association']=='CEN') | (df_complete['Country Association']=='CENELEC')]
        CA_EU_EEA_df.to_excel(str(path_engineers)+'\\CountryAssociation_EU_EEA.xlsx', index=False)
        CA_CEN_CENELEC_df.to_excel(str(path_engineers)+'\\CountryAssociation_CEN_CENELEC.xlsx', index=False)            

#main



df = combine()

df=df.loc[~df['Regulation Title (EN)'].str.contains('toys|vehicle|vehicles',case=False, na=False)]

df_national_laws,df_shared_laws= dataframes(df)

df_shared_laws_sorted = df_shared_laws_sorted(df_shared_laws,lst1)
temp=utilities(lst1) # temp is of class countries

df_complete=df_shared_laws_sorted.groupby(['ID', 'Revision ID', 'Name', 'Regulation Title (EN)', 'Reference Number', 'Country Association', 'Country', 'Enforcement Status', 'Duplicate Process Status', 'Extra'], dropna=False)['Checked For Country'].apply(', '.join).reset_index()
df_complete.rename(columns={"Checked For Country": "Shared Countries"}, inplace=True)
temp.market_specialists_engineers(df_complete,df,lst1,df_national_laws)
df_national_laws.to_excel(str(path_output)+'\\National.xlsx', index=False)
common_regs_df=temp.common_regs(df)
common_regs_df.to_excel(str(path_output)+'\\Common-regs.xlsx', index=False)


