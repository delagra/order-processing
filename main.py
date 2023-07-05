import pandas as pd
import re
#open file
df = pd.read_csv('c:\\users\\Vlade\\Test3.csv', index_col=None)
#extract Color/Finish
def extract_color_finish(string):
    match = re.search(r"(Color/Finish\s+)(\w+)", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(2)
#add columns
df['Font'] = ""
df['Letter 1'] = ""
df['Text 1']= ""
df['Text 2']= ""
df['Text 3']= ""
df['Text 4']= ""
df['Color']= ""


for index, row in df.iterrows():

    if row['Order Number'] > 1000000000:
        #extract Color/Finish
        df.at[index,'Color'] = extract_color_finish(row['Item Name'])
        print(row['Order Number'])
        #extract Personalization
        #check SKU "-02"
print(df)