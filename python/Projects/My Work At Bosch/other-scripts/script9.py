# First we import the module panda as pd
import pandas as pd
import re

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\PythonTest\extra\uk.xlsx')

#df.sort_values(['Country'], ascending=True, inplace=True) # Sort in ascending order according to countries

EU_UK_df=df.loc[df['Country Association'].str.contains('EU', na=False) & df['Country'].str.contains('United Kingdom', na=False) & ~df['Country Association'].str.contains('EEA', na=False)]
UK_df1=df.loc[df['Country'] == 'Austria (AT),Belgium (BE),Bulgaria (BG),Cyprus (CY),Czechia (CZ),Germany (DE),Denmark (DK),Estonia (EE),Spain (ES),Finland (FI),France (FR),Greece (GR),Croatia (HR),Hungary (HU),Ireland (IE),Italy (IT),Lithuania (LT),Luxembourg (LU),Latvia (LV),Malta (MT),Netherlands (NL),Poland (PL),Portugal (PT),Romania (RO),Sweden (SE),Slovenia (SI),Slovakia (SK)'] #EU
UK_df2=df.loc[df['Country'] == 'Austria (AT),Belgium (BE),Bulgaria (BG),Cyprus (CY),Czechia (CZ),Germany (DE),Denmark (DK),Estonia (EE),Spain (ES),Finland (FI),France (FR),Greece (GR),Croatia (HR),Hungary (HU),Ireland (IE),Iceland (IS),Italy (IT),Liechtenstein (LI),Lithuania (LT),Luxembourg (LU),Latvia (LV),Malta (MT),Netherlands (NL),Norway (NO),Poland (PL),Portugal (PT),Romania (RO),Sweden (SE),Slovenia (SI),Slovakia (SK)'] #EU and EEA
frames = [df, UK_df1, UK_df2]
result_df = pd.concat(frames,axis=0) # this dataframe is the dataframes 'UK_df1' and 'UK_df2' substracted from 'EU_UK_df'
result_df.drop_duplicates(keep=False, inplace=True) # drop duplicates including original


UK_df1.reset_index(drop=True, inplace=True)
UK_df2.reset_index(drop=True, inplace=True)
result_df.reset_index(drop=True, inplace=True)
EU_UK_df.reset_index(drop=True, inplace=True)
#print(len(EU_EEA_exclusive_df.index))    
#print(len(EU_EEA_common_df.index))
#print(len(EU_df.index))
#print(len(EEA_df.index))
print(len(UK_df2['ID']))
print(len(UK_df1['ID']))
print(len(df['ID']))
print(result_df['ID'])
print('Regulations in UK coming under EU with EEA excluded (only EU) \n', EU_UK_df['ID'])


# To compare country associations
list1='Austria (AT),Australia (AU),Belgium (BE),Bulgaria (BG),Brazil (BR),Switzerland (CH),China (CN),Cyprus (CY),Czechia (CZ),Germany (DE),Denmark (DK),Estonia (EE),Spain (ES),Finland (FI),France (FR),United Kingdom (GB),Greece (GR),Croatia (HR),Hungary (HU),Ireland (IE),India (IN),Italy (IT),Lithuania (LT),Luxembourg (LU),Latvia (LV),Malta (MT),Netherlands (NL),Poland (PL),Portugal (PT),Romania (RO),Sweden (SE),Slovenia (SI),Slovakia (SK),USA (US)' #EU with UK
list2='Austria (AT),Belgium (BE),Bulgaria (BG),Cyprus (CY),Czechia (CZ),Germany (DE),Denmark (DK),Estonia (EE),Spain (ES),Finland (FI),France (FR),Greece (GR),Croatia (HR),Hungary (HU),Ireland (IE),Italy (IT),Lithuania (LT),Luxembourg (LU),Latvia (LV),Malta (MT),Netherlands (NL),Poland (PL),Portugal (PT),Romania (RO),Sweden (SE),Slovenia (SI),Slovakia (SK)' #EU normal countries
list1=list1.split(',')
list2=list2.split(',')

for item in list1:
    if item in list2:
        #print('match',str(item))
        x=1
    else:
        print('not match',str(item))
