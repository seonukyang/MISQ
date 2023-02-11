from doctest import DocFileSuite
import pandas as pd
import numpy as np
import datetime
import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

year_list=['1977-1984','1985-1989','1990-1994','1995-1999','2000-2004','2005-2009','2010-2014','2015-2019','2020-2022']
#출력 데이터프레임 정의
df_count = {'year':[],'keyword':[],'method':[],'theory':[]}
df_count = pd.DataFrame(df_count)



for year in year_list : 
    df = pd.read_csv('fellowship_data_20220520/topic'+year+'_20220520.csv').fillna(value='nan')
    keyword = []
    method = []
    theory = []

    keyword_count = 0
    method_count = 0
    theory_count = 0

    for i in range(0,len(df['keyword']),1) :
        if df['keyword'].iloc[i] != 'nan' : 
            for j in range(0, len(df['keyword'].iloc[i].split(',')),1) : 
                keyword_split = df['keyword'].iloc[i].split(',')[j]
                keyword.append(keyword_split)

    for i in range(0,len(df['method']),1) : 
        if df['method'].iloc[i] != 'nan' :
            for j in range(0, len(df['method'].iloc[i].split(',')),1) : 
                method_split = df['method'].iloc[i].split(',')[j]
                method.append(method_split)

    for i in range(0,len(df['theory']),1) : 
        if df['theory'].iloc[i] != 'nan' :
            for j in range(0, len(df['theory'].iloc[i].split(',')),1) : 
                theory_split = df['theory'].iloc[i].split(',')[j]
                theory.append(theory_split)

    print(keyword)
    keyword_count = len(keyword)
    method_count = len(method)
    theory_count = len(theory)
  
            
    newdata = {'year':year, 'keyword': keyword_count, 'method': method_count ,'theory' :theory_count}
    df_count = df_count.append(newdata, ignore_index=True)


now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
df_count.to_csv('keyword_count_resultdata'+today+'.csv', encoding='utf-8-sig')
# print(df_count)