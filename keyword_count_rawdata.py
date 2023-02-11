from doctest import DocFileSuite
import pandas as pd
import numpy as np
import datetime
import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

year_list=['1977-1984','1985-1989','1990-1994','1995-1999','2000-2004','2005-2009','2010-2014','2015-2019','2020-2022']
#출력 데이터프레임 정의
df_count = {'year':[],'keyword':[]}
df_count = pd.DataFrame(df_count)

for year in year_list : 
    df = pd.read_excel('raw data_220520.xlsx', sheet_name=year)

    keyword_count = 0
    method_count = 0
    theory_count = 0
    for i in range(0, len(df['keyword']),1):
        keyword_num = len(str(df['keyword'].iloc[i]).split(','))
        keyword_count = keyword_count + keyword_num

            
    newdata = {'year':year, 'keyword': keyword_count}
    df_count = df_count.append(newdata, ignore_index=True)


now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
df_count.to_csv('keyword_count_rawdata'+today+'.csv', encoding='utf-8-sig')
# print(df_count)