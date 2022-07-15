import numpy as py;
import pandas as pd;
from fuzzywuzzy import fuzz;

df_dummydata1 = pd.read_csv (r'C:\Users\stefan.guler\OneDrive - BearingPoint GmbH\Desktop\fuzzydummydata1.csv')
df_dummydata2 = pd.read_csv (r'C:\Users\stefan.guler\OneDrive - BearingPoint GmbH\Desktop\fuzzydummydata2.csv')
print (df_dummydata1)
print (df_dummydata2)

y = 1
x = 1

for gp1 in df_dummydata1.iloc[:,1]:
    print(f"------------- Start GP {gp1} check --------------")
    for gp2 in df_dummydata2.iloc[:,y]:
        if x <= 4:
            print(f"------------- Start Col {df_dummydata2.iloc[:,x].name} check --------------")
            for gp2 in df_dummydata2.iloc[:,x]:
                    Token_Set_Ratio = fuzz.token_set_ratio(gp1,gp2)
                    print(f'fuzzycheck: GP1 as {gp1} vs GP2 {gp2} results in {Token_Set_Ratio}% similarity')
            print(f"------------- End Col {df_dummydata2.iloc[:,x].name} check --------------\n")
            x = x+1
    y = y+1
    x = 1
    