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
def extract_personalization(string):
    match = re.search(r'Personalization\s+(.*)', string, re.IGNORECASE)
    if match:
        return match.group(1)

def check_02(string):
    match = re.search(r'-02$', string, re.IGNORECASE)
    if match:
        return "Cambria"

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
        # extract Personalization
        df.at[index, 'Text 1'] = extract_personalization(row['Item Name'])
        # check SKU "-02"
        df.at[index, 'Font'] = check_02(row['SKU'])

print(df['Font'])