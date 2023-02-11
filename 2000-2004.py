from doctest import DocFileSuite
import pandas as pd
import numpy as np

df = pd.read_excel('raw data_1230.xlsx', sheet_name='2000-2004')
switch = pd.read_excel('switch.xlsx', sheet_name='Switch')
# country = pd.read_excel('.xlsx', sheet_name='Sheet1')
category = pd.read_excel('switch.xlsx', sheet_name='Category')



#국가 단어 삭제
# for i in range(0, len(df),1) : 
#     for j in range(0, len(df.loc[i]),1) : 
#             for k in range(0, len(country),1) : 
#                 if df.loc[i][j] == country['county'].loc[k] : 
#                     del df.loc[i][j]


#축약어 변환
for i in range(0,len(df),1) : 
    text = df.loc[i][0].lower().split(', ')
    for j in range(0, len(text),1) : 
        for k in range(0, len(switch),1) : 
            if text[j].replace(' ','') == switch['before'].iloc[k] : 
                text[j] = switch['after'].iloc[k]
    df.loc[i][0] = text[:]

#주제어, 방법론, 이론 분류
df_category = {'keyword':[],'method':[],'theory':[]}
df_category = pd.DataFrame(df_category)
for i in range(0,len(df),1) : 
    text = df.loc[i][0]
    keyword = df.loc[i][0]
    method = []
    theory = []

    target_num = 100
    for j in range(0, len(text),1) :
        text_filter = str(text[j]).lower().replace(' ','') 
        for k in range(0, len(category['method_fil']),1) :      
            if len(text_filter.split(str(category['method_fil'].iloc[k]).replace(' ','')))>1  and target_num==100:
                target_num = j
                method.append(text[j])
    if target_num != 100 : 
        del text[target_num] 
    
    
    target_num = 100
    for j in range(0, len(text),1) :
        text_filter = str(text[j]).lower().replace(' ','') 
        for k in range(0, len(category['method_before']),1) : 
            if len(text_filter.split(str(category['method_before'].iloc[k]).replace(' ','')))>1  and target_num==100:
                target_num = j
                method.append(category['method_after'].iloc[k])
    if target_num != 100 : 
        del text[target_num] 


    target_num = 100
    for j in range(0, len(text),1) :
        text_filter = str(text[j]).lower().replace(' ','') 
        for k in range(0, len(category['theory_fil']),1) : 
            if len(text_filter.split(str(category['theory_fil'].iloc[k]).replace(' ','')))>1  and target_num==100:
                target_num = j
                theory.append(text[j])
    if target_num != 100 : 
        del keyword[j]

    target_num = 100
    for j in range(0, len(text),1) :
        text_filter = str(text[j]).lower().replace(' ','') 
        for k in range(0, len(category['theory_before']),1) : 
            if len(text_filter.split(str(category['theory_before'].iloc[k]).replace(' ','')))>1  and target_num==100:
                target_num = j
                theory.append(category['theory_after'].iloc[k])
    if target_num != 100 : 
        del text[j]

    keyword = text[:]
    newdata = {'keyword': str(keyword).replace('\'','').replace('[','').replace(']',''), 
    'method': str(method).replace('\'','').replace('[','').replace(']',''), 
    'theory': str(theory).replace('\'','').replace('[','').replace(']','')}
    df_category = df_category.append(newdata, ignore_index=True)

# for i in range(0, len(df_category),1) : 
#     df_category['keyword'].iloc[i] = str(df_category['keyword'].iloc[i]).replace('\'','').replace('[','').replace(']','')
#     df_category['method'].iloc[i] = str(df_category['method'].iloc[i]).replace('\'','').replace('[','').replace(']','')
#     df_category['theory'].iloc[i] = str(df_category['theory'].iloc[i]).replace('\'','').replace('[','').replace(']','')
df_category.to_csv('category_2000-2004.csv', encoding='utf-8-sig')