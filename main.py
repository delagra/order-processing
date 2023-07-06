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

def get_color(string):
    match = re.search(r"(Color:\s+)(\w+)", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(2)
def get_name(string):
    match = re.search(r"Name: \(Please limit to one word\)(.*?)Choose", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)
def get_text(string):
    match = re.search(r"Custom Text:(.*?)Choose", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)
def get_top(string):
    match = re.search(r"\(Top\):(.*?)Choose", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)
def get_center(string):
    match = re.search(r"\(Center\):(.*?)Choose", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)
def get_bottom(string):
    match = re.search(r"\(Bottom\):(.*?)Choose", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)

def get_font(string):
    match = re.search(r"(Choose your Font:\s+)(\w+)", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(2)
def get_comment(string):
    match = re.search(r"Customer Note:(.*?)_customily", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)
def get_letter(string):
    match = re.search(r"Letter:\s+(\S)", string, re.IGNORECASE)
    if match:
        if match.span():
            return match.group(1)
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
    if row['Order Number'] < 1000000000:
        df.at[index, 'Color'] = get_color(row['Item Name'])
        text1 =get_name(row['Item Name']) or get_text(row['Item Name']) or get_top(row['Item Name'])
        df.at[index, 'Text 1'] = text1
        df.at[index, 'Font'] = get_font(row['Item Name'])
        df.at[index, 'Customer Comments'] = get_comment(row['Item Name'])
        df.at[index, 'Letter'] = get_letter(row['Item Name'])
        df.at[index, 'Text 2'] = get_center(row['Item Name'])
        df.at[index, 'Text 3'] = get_bottom(row['Item Name'])
df.to_excel('output.xlsx')