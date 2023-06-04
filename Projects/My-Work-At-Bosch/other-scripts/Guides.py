# First we import the module panda as pd
import pandas as pd



# To read the excel file

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\C2P+NORMASTER+GUIDANCE+STANDARDS\NationalLaws-automatic-Normmaster+C2P.xlsx')



# To Print all columns

#print(df.columns)




# To Print last 5 column or raw? -- check lol

#print(df.tail(5))



# To Print the column 'Austria'

#print(df['Austria']) 



# To Print the column 'Austria' from first raw to fifth

#print(df['Austria'][0:5]) 



# To Print the column 'Austria' and 'CH' from first raw to fifth

#print(df[['Austria','CH']][0:5]) 



# To Print raw 1 to 4

#print(df.iloc[1:4]) 



# To Print a cell

#print(df.iloc[2,1]) 



# To display raws with value REG_00498517

#df.loc[df['Total (without Null values)'] == "REG_00498517" ] 



# To list out every raw in for loop 

#for index, row in df.iterrows():     
#    print(index,row)



# To sort values in columns 'Austria' and 'CH' where 'Austria' is ascending and 'CH' is in descending but also only first 5 elemnts

#df.sort_values(['Austria', 'CH'], ascending=[1,0][0:5])



# To delete column 'Austria'

#df = df.drop(columns=['Austria', 'CH'])   



# To list out 5 raws in for loop 


#i=0
#for index, row in df.iterrows():  
#    i=i+1
#    if (i<5):
#        print(index,row)
#    else:
#        break

        
# To add a new column Total and defining as the sum of raws 4 to 9. in iloc function we use ':', it means include all rows. axis =1 means sum is done horizontally. 4:9 means adding raws 4 to 9.


#df['Total'] = df.iloc[:, 4:9].sum(axis=1)





# To rearrange columns. First line is from documentation. 2nd line says, keep columns 0 to 4 intact and then add last column then keep the rest as it is

#cols= list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]




# To display raws with value poland = REG_00016679 and croatia= REG_00487675. Use "|" for 'or'

#df.loc[(df['Poland'] == 'REG_00016679') & (df['Croatia'] == 'REG_00487675') | (df['Slovakia'] == 'REG_00020098')]



# You can also combine more than two arguments. Here, for example the first two arguments are evaluted before the third one

#df.loc[(df['Poland'] == 'REG_00016679') & (df['Croatia'] == 'REG_00487675') | (df['Slovakia'] == 'REG_00020098')]





# To store it to a new dataframe.

#new_df = df.loc[(df['Poland'] == 'REG_00016679') & (df['Croatia'] == 'REG_00487675') | (df['Slovakia'] == 'REG_00020098')]






# To export it

#df.reset_index(drop=True, inplace=True)
#df.to_excel('Modified.xlsx', index=False)



# To only include cells containing certain values. Note: Use int instaed of str if you want to filter out integer of the value. We use na=false for 'nan' values in Excel file. 

#df.loc[df['Poland'].str.contains('REG_001', na=False)]




# To filter out cells containing certain values. We use negate. This command only lists 1 to 20. 

#df.loc[~df['Poland'].str.contains('REG_001', na=False)][1:20]





# To filter out cells with multiple conditions. 

#import re
#df.loc[~df['Poland'].str.contains('REG_001|REG_002', na=False)][1:20]





# To filter out cells with multiple conditions and ignore case sensitivity 

#import re
#df.loc[~df['Poland'].str.contains('REG_001|REG_002', flags=re.I, na=False)][1:20]






# To start with REG_001 and end with any other characters. Note: Dont use '^', if you want to have REG_001 anywhere in the column 'Poland'

#import re
#df.loc[df['Poland'].str.contains('^REG_0001[a-z]*', flags=re.I, na=False)]







# To rename a column based on a condition, say if Column 'poland' has value 'REG_00582918' in it we rename it to deleted.

#df.loc[df['Poland'] == 'REG_00582918', 'Poland'] = 'Deleted'
#print(df.iloc[1:40]) 





# To rename a column based on a condition, say if Column 'poland' has value 'REG_00582918' in it, we put another value for another column (column 'Austria' to 'deleted').

#df.loc[df['Poland'] == 'REG_00582918', 'Austria'] = 'Deleted'
#print(df.iloc[1:40]) 




# To rename a column based on a condition, say if Column 'poland' has value 'REG_00582918' in it, we modify 2 other columns (column 'Austria' to 'deleted1' and column 'CH' to 'deleted2').

#df.loc[df['Poland'] == 'REG_00582918', ['Austria','CH']] = ['Deleted1','Deleted2']
#print(df.iloc[1:40]) 


# To group by based on number of regulations (duplication)
# df.groupby(['Total (without Null values)']).count()[1:30]



# To list every raws based on count
# First we define a new column and give it a value 1
df['count']=1
df.groupby(['Austria', 'CH']).count()['count']