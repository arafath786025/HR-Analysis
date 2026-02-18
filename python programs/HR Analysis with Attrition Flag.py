#import pandas

import pandas as pd

#import file

df = pd.read_csv("E:\Project\HR Analysis\Dataset\HR Analysis.csv")

#create attrition flag column

df['Attrition_Flag'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

#save oupt in excel format

df.to_excel("HR_Analysis_With_AttritionFlag.xlsx", index=False)
