from doctest import DocFileSuite
from re import A
import pandas as pd
import numpy as np
import datetime

change = pd.read_excel('switch_220419.xlsx', sheet_name='Change').fillna(value='hisashiburi')

df_keyword = {'keyword':[]}
df_keyword = pd.DataFrame(df_keyword)

df_method = {'method':[]}
df_method = pd.DataFrame(df_method)

df_theory = {'theory':[]}
df_theory = pd.DataFrame(df_theory)
   

year_list=['1977-1984','1985-1989','1990-1994','1995-1999','2000-2004','2005-2009','2010-2014','2015-2019','2020-2022']
for year in year_list : 

    df = pd.read_csv('fellowship_data_20220521/topic'+year+'_20220521.csv').fillna(value='nan')

    for i in range(0,len(df['keyword']),1) : 
        if df['keyword'].iloc[i] != 'nan' :
            keyword_split = str(df['keyword'].loc[i]).lower().replace(' ','').replace('-','').split(',')
            for j in range(0,len(keyword_split)) :    
                newdata = {'keyword': keyword_split[j]} 
                df_keyword = df_keyword.append(newdata, ignore_index=True)

    for i in range(0,len(df['method']),1) : 
        if df['method'].iloc[i] != 'nan' :
            method_split = str(df['method'].loc[i]).lower().replace(' ','').replace('-','').split(',')
            for j in range(0,len(method_split)) :   
                newdata = {'method': method_split[j]}
                df_method = df_method.append(newdata, ignore_index=True)

    for i in range(0,len(df['theory']),1) : 
        if df['theory'].iloc[i] != 'nan' :
            theory_split = str(df['theory'].loc[i]).lower().replace(' ','').replace('-','').split(',')
            for j in range(0,len(theory_split)) :    
                newdata = {'theory': theory_split[j]}
                df_theory = df_theory.append(newdata, ignore_index=True)


    now = datetime.datetime.now()
    today = now.strftime('%Y%m%d')
    df_keyword.to_csv('analysis_keyword'+year+'_'+today+'.csv', encoding='utf-8-sig')
    df_method.to_csv('analysis_method'+year+'_'+today+'.csv', encoding='utf-8-sig')
    df_theory.to_csv('analysis_theory'+year+'_'+today+'.csv', encoding='utf-8-sig')

