# For splitting 'country' column into multiple columns


import pandas as pd
df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\PythonTest\extra\Austria.xlsx') 


# creating a new column 'Countris_Split' to store the splitted columns based on the seprator 'comma'
df['Countris_Split'] = df['Country'].str.split(',')



# Create a new dataframe 'df_countries' to store the 'Countris_Split' column and store them to the name Country '0-n'
df_countries = pd.DataFrame(df['Countris_Split'].tolist()).fillna('').add_prefix('Country_')

# Combine the new dataframe 'df_countries' with the old dataframe 'df'
df = pd.concat([df, df_countries], axis=1)
df.to_excel('Modified.xlsx', index=False) # export to excel





#To get split view basedd on commas

#lst3=cell.split(',')
#for item in lst3:
#    print(item)
  