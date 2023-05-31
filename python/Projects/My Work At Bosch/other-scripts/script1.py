# First we import the module panda as pd
import pandas as pd



# To read the excel file without na values

#df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\C2P+NORMASTER+GUIDANCE+STANDARDS\NationalLaws-automatic-Normmaster+C2P.xlsx', keep_default_na=False)


# To read the excel file

df = pd.read_excel(r'C:\Users\JOT1WE\Desktop\Test\C2P+NORMASTER+GUIDANCE+STANDARDS\NationalLaws-automatic-Normmaster+C2P.xlsx')


# To replace na values with 0. Use it when, 'keep_default_na' is not specified
df=df.fillna(0)



#length of columns
print(len(df.columns))


i=0
#display individual columns
for column_toc in df.columns:             # loops through columns. 'df.columns' output individual columns and is then passed to varaiable 'column_toc' 
    print("xx")                           # A spacer for easily distinguishing when a column is over
    for cell_toc in df[column_toc]:       # loops through each element of the column "column_toc". df["column"] provides each element of the column
        if len(str(cell_toc)) == 12:      # All regulations have 12 digits. We can also use 'begins with REG_ **' as another if condition
            k=0                           # A variable to provide index numbers
            i=i+1
            print('Comparing:', cell_toc)
            for column_comp in df.columns:
                for cell_comp in df[column_comp]:          # This nexted 'for loop' also does the same as the for loop before it. It takes evrey element in the dataframe
                    if (str(cell_toc)==str(cell_comp) and  len(str(cell_comp)) == 12 and column_toc!=column_comp) :                  #if duplication occures between regulations. The 'column_toc!=column_comp' is for not comparing same columns.
                        k=k+1
                        print('Occurs in', column_comp, 'with element', cell_toc, 'with index', k)