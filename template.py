import numpy as py;
import pandas as pd;
from fuzzywuzzy import fuzz;

#import two table where you want to do fuzzy comparison
df_dummydata1 = pd.read_csv (r'path')
df_dummydata2 = pd.read_csv (r'path')

#print to check
print (df_dummydata1)
print (df_dummydata2)

x = 1

#adressing specific cols in the table, related to the case that had to be solved - scope to be adjusted here if required // most outer loop (current: first second col in table df_dummydata1)
for val1 in df_dummydata1.iloc[:,1]:
    print(f"------------- Start GP {val1} check --------------")
    #adressing specific cols in the table, related to the case that had to be solved - scope to be adjusted here if required // inner outer loop (current: 2nd to 4th col in table df_dummydata2)
    for col in df_dummydata2.iloc[:,x]:
        if x <= 4:
            print(f"------------- Start Col {df_dummydata2.iloc[:,x].name} check --------------")
            #adressing specific values in cols in the table, related to the case that had to be solved - scope to be adjusted here if required // inner inner loop (current: all values within 2nd to 4th col in table df_dummydata2)
            for val2 in df_dummydata2.iloc[:,x]:
                    Token_Set_Ratio = fuzz.token_set_ratio(val1,val2)
                    print(f'fuzzycheck: GP1 as {val1} vs GP2 {val2} results in {Token_Set_Ratio}% similarity')
            print(f"------------- End Col {df_dummydata2.iloc[:,x].name} check --------------\n")
        #next col if all comparison in current col are done
        x = x+1
    #reset x position to restart at col 1 for next dataset
    x=1
    