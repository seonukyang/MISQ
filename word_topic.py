from doctest import DocFileSuite
import pandas as pd
import numpy as np
import datetime
import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

year_list=['1977-1984','1985-1989','1990-1994','1995-1999','2000-2004','2005-2009','2010-2014','2015-2019','2020-2022']
# year_list=['1977-1984']
category = pd.read_excel('switch_220519.xlsx', sheet_name='Code').fillna(value='hisashiburi')
#축약어 변환
def short_word_change(word_list) : 
    new_word_list = []
    for i in range(0,len(word_list),1) :
        new_word = str(word_list[i]).split('(')
        if len(new_word)>1 : 
            new_word_list.append(new_word[1].replace(')',''))
        else : new_word_list.append(new_word[0])
    return new_word_list

#축약어 삭제
def short_word_delete(word_list) : 
    new_word_list = []
    for i in range(0,len(word_list),1) :
        new_word = str(word_list[i]).split('(')
        if len(new_word)>1 : 
            new_word_list.append(new_word[0].replace(')',''))
        else : new_word_list.append(new_word[0])
    return new_word_list


#keyword_before과 일치여부
def keyword_before_same(text_filter) : 
    for k in range(0, len(category['keyword_before']),1):
        test_word = str(category['keyword_before'].iloc[k]).lower().replace('/','').replace('-','').replace(' in ',' ').replace(' of ',' ').replace(' and ',' ').replace(' ','')
        if text_filter == test_word : 
            for i in range(0, len(keyword), 1): 
                if str(keyword[i]) == test_word :  
                    del keyword[i]
            for u in range(0,len(topic['keyword_before']),1) : 
                if category['keyword_after'].iloc[k] == topic['keyword_before'].iloc[u] : 
                    keyword.append(topic['keyword_after'].iloc[u])
                    return False          
            keyword.append(category['keyword_after'].iloc[k])
            return False          
        else : 
            for u in range(0,len(topic['keyword_before']),1) : 
                if text_filter == topic['keyword_before'].iloc[u] : 
                    for i in range(0, len(keyword), 1): 
                        if str(keyword[i]) == text_filter :  
                            del keyword[i]
                            break
                    keyword.append(topic['keyword_after'].iloc[u])
                    return False                   
    return True

#method_fil과 일치여부, 부분일치여부
def method_fil_same(text_filter) :
    for k in range(0, len(category['method_fil']),1) : 
        test_word = str(category['method_fil'].iloc[k]).lower().replace('/','').replace('-','').replace(' in ',' ').replace(' of ',' ').replace(' and ',' ').replace(' ','')
        if text_filter == test_word : 
            keyword_del(text_filter)
            for u in range(0,len(topic['method_before']),1) : 
                if text_filter == topic['method_before'].iloc[u] : 
                    method.append(topic['method_after'].iloc[u])
                    return False         
            method.append(text_filter)
            return False   

        elif len(text_filter.split(test_word))>1 : 
            keyword_del(text_filter)
            for u in range(0,len(topic['method_before']),1) : 
                if text_filter == topic['method_before'].iloc[u] : 
                    method.append(topic['method_after'].iloc[u])
                    return False
            method.append(text_filter)
            return False   
    return True

#method_before과 일치여부
def method_before_same(text_filter) : 
    for k in range(0, len(category['method_before']),1):
        test_word = str(category['method_before'].iloc[k]).lower().replace('/','').replace('-','').replace(' in ',' ').replace(' of ',' ').replace(' and ',' ').replace(' ','')
        if text_filter == test_word : 
            keyword_del(text_filter)
            for u in range(0,len(topic['method_before']),1) : 
                if category['method_after'].iloc[k] == topic['method_before'].iloc[u] : 
                    method.append(topic['method_after'].iloc[u])
                    return False                  
            method.append(category['method_after'].iloc[k])
            return False
    return True

#theory_fil과 일치여부, 부분일치여부
def theory_fil_same(text_filter) :
    for k in range(0, len(category['theory_fil']),1) : 
        test_word = str(category['theory_fil'].iloc[k]).lower().replace('/','').replace('-','').replace(' in ',' ').replace(' of ',' ').replace(' and ',' ').replace(' ','')
        if text_filter == test_word : 
            keyword_del(text_filter)
            for u in range(0,len(topic['theory_before']),1) : 
                if text_filter == topic['theory_before'].iloc[u] : 
                    theory.append(topic['theory_after'].iloc[u])
                    return False                  
            theory.append(text_filter)
            return False   

        elif len(text_filter.split(test_word))>1 : 
            keyword_del(text_filter)
            for u in range(0,len(topic['theory_before']),1) : 
                if text_filter == topic['theory_before'].iloc[u] : 
                    theory.append(topic['theory_after'].iloc[u])
                    return False                   
            theory.append(text_filter)
            return False
    return True

#theory_before과 일치여부
def theory_before_same(text_filter) : 
    for k in range(0, len(category['theory_before']),1):
        test_word = str(category['theory_before'].iloc[k]).lower().replace('/','').replace('-','').replace(' in ',' ').replace(' of ',' ').replace(' and ',' ').replace(' ','')
        if text_filter == test_word : 
            keyword_del(text_filter)
            for u in range(0,len(topic['theory_before']),1) : 
                if category['theory_after'].iloc[k] == topic['theory_before'].iloc[u] : 
                    theory.append(topic['theory_after'].iloc[u])
                    return False                  
            theory.append(category['theory_after'].iloc[k])
            return False
    return True


#keyword에서 단어 제거
def keyword_del(word) : 
    i=0
    end = len(keyword)
    while i<end : 
        if str(word).replace(' ','') == str(keyword[i]).replace(' ','') : 
            del keyword[i]
            break
        i = i+1

#keyword에서before단어로 after단어로 변경
# def keyword_before_after(word, k) : 
#     i=0
#     end = len(category['keyword_before'])
#     while i<end : 
#         if word.replace(' ','') == category['keyword_after'].iloc[i].lower().replace(' ','') : 
#             keyword[k] = category['keyword_after'].iloc[i]
#             break
#         i = i+1


#국가 단어 삭제
def country_del(text_filter, text) : 
    for k in range(0, len(category['country']),1):
        test_word = str(category['country'].iloc[k]).lower().replace('/','').replace('-','').replace(' in ',' ').replace(' of ',' ').replace(' and ',' ').replace(' ','')
        if text_filter == test_word : 
            keyword_del(text)
            return False
    return True


for year in year_list : 
    df = pd.read_excel('raw data_220520.xlsx', sheet_name=year)
    df = df.dropna()
    topic = pd.read_excel('topic_220520.xlsx', sheet_name=year).fillna(value='hisashiburi')
    
    #출력 데이터프레임 정의
    df_category = {'keyword':[],'method':[],'theory':[]}
    df_category = pd.DataFrame(df_category)


    #주제어, 방법론, 이론 분류
    for i in range(0,len(df['keyword']),1) :
    # for i in range(62,63,1) :
        text_list = df['keyword'].iloc[i].replace(' vs. ',',').replace(':','').replace('-',' ').replace('\'','').replace('/',',').replace('&',',').replace(' and ',',').replace(';',',').split(',')
        keyword = []
        method = []
        theory = []

        # keyword = short_word_change(keyword)
        # method = short_word_change(method)
        # theory = short_word_change(theory)
        
        text_list = short_word_delete(text_list)


        for j in range(0, len(text_list),1) :
        # for j in range(0, 3,1) :

            text_list[j] = text_list[j].replace('/','').replace(' in ',' ').replace(' of ',' ')
            text_list[j] = lemmatizer.lemmatize(text_list[j])

            text_filter = str(text_list[j]).lower().replace(' ','')

            keyword.append(text_filter)
            if country_del(text_filter, text_list[j]) == True:
                if keyword_before_same(text_filter) == True : 
                    if method_before_same(text_filter) == True :
                        if method_fil_same(text_filter) == True : 
                            if theory_before_same(text_filter) == True : 
                                theory_fil_same(text_filter)                
            
        newdata = {'keyword': str(keyword).replace('\'','').replace('[','').replace(']',''), 
        'method': str(method).replace('\'','').replace('[','').replace(']',''), 
        'theory': str(theory).replace('\'','').replace('[','').replace(']','')}
        df_category = df_category.append(newdata, ignore_index=True)


    now = datetime.datetime.now()
    today = now.strftime('%Y%m%d')
    df_category.to_csv('topic'+year+'_'+today+'.csv', encoding='utf-8-sig')
