import numpy as np
import pandas as pd

air = 220000
cake = 58000
flower = 30000

cost = air+cake+flower

master_num = 8
grade_num = 9


plesent_doc = {'cost':[], 'master_total_money':[],'master_per_money':[], 'grade_total_money':[],'grade_per_money':[]}
df_plesent = pd.DataFrame(plesent_doc)

for i in range(0,int(cost/1000),1) : 
    master_per_money = 1000*i
    master_total_money = 1000*i*master_num
    grade_total_money = cost - master_total_money
    grade_per_money = grade_total_money/grade_num
    
    newdata = {'cost':cost, 'master_total_money':master_total_money,'master_per_money':master_per_money,'grade_total_money':grade_total_money, 'grade_per_money':grade_per_money}
    df_plesent = df_plesent.append(newdata, ignore_index=True)
df_plesent.to_csv('plesent.csv', encoding='utf-8-sig')