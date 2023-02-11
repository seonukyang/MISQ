import pandas as pd
import numpy as np
import urllib.request
from bs4 import BeautifulSoup as bs
import re
from selenium import webdriver
from pandas.io.html import read_html
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# df = pd.read_csv('search_link3.csv', encoding='utf-8')
# df = pd.read_csv('crawling_result3.0.200.csv', encoding='utf-8')
# df = pd.read_csv('crawling_result3.200.400.csv', encoding='utf-8')
# df = pd.read_csv('crawling_result3.400.800.csv', encoding='utf-8')
# df = pd.read_csv('crawling_result3.800.1600.csv', encoding='utf-8')
# df = pd.read_csv('crawling_result3.1600.2200.csv', encoding='utf-8')
df = pd.read_csv('crawling_result3.2200.2600.csv', encoding='utf-8')

#변수선언
# df['project'] = ''
# df['token_name'] = ''
# df['rating'] = ''
# df['type'] = ''
# df['industy'] = ''
# df['whitelist'] = ''
# df['KYC'] = ''
# df['soft_cap'] = ''
# df['hard_cap'] = ''
# df['tokens_for_sale'] = ''
# df['price'] = ''
# df['min'] = ''
# df['max'] = ''
# df['bounty'] = ''
# df['whitepaper'] = ''
# df['currencies'] = ''
# df['platform'] = ''
# df['token_standard'] = ''
# df['role_of_token'] = ''
# df['location'] = ''
# df['restricted_areas'] = ''
# df['social_medial'] = ''
# df['start'] = ''
# df['end'] = ''
# df['received'] = ''
# df['bonuses'] = ''
# df['team'] = ''
# df['advisors'] = ''

for i in range(2600, len(df['link']), 1) :
# for i in range(0, 200, 1) :
# for i in range(200, 400, 1) :
# for i in range(400, 800, 1) :
# for i in range(1600, 2200, 1) :
# for i in range(2200, 2600, 1) :

    print(df['id'].loc[i])
    url = df['link'].loc[i]
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = bs(html, 'html.parser')
 
    #project, token_name
    tags = soup.select('#ico-head-cont > div > div.col-xs-12.col-sm-9.col-md-9.col-lg-9')
    element_list = []
    for tag in tags :
        element_list.append(tag.text)
    project_element = element_list[0].replace('\n','').split(' (')[0]
    df['project'].loc[i]=project_element

    if element_list[0].replace('\n','') != element_list[0].replace('\n','').split(' (')[0] : 
        token_name_element = element_list[0].replace('\n','').split(' (')[1].split(') ')[0]
        df['token_name'].loc[i] = token_name_element
    else : df['token_name'].loc[i] = ''
    
    

    #rating
    tags = soup.select('.flmf-mark')
    element_list = [0]
    for tag in tags :
        element_list.append(tag.text)
    if len(element_list) > 1 : 
        rating_element = element_list[1].replace('?','')
        df['rating'].loc[i]=rating_element
    else : df['rating'].loc[i] = ''

    #type, industy, whitelist, KYC, soft_cap, hard_cap, tokens_for_sale, price, min, max, bounty, whitepaper, currencies, platform, token_standard, role_of_token
    #location, restricted_areas, social_medial, bonuses
    tags = soup.select('.smry-table')
    element_list = []
    for tag in tags :
        element_list.append(tag.text)

    if element_list[0] != element_list[0].split('Type:')[0] : 
        type_element = element_list[0].split('Type:')[1].split('Category:')[0].replace('\n','')
        df['type'].loc[i]=type_element
    else : df['type'].loc[i]= ''

    industy_element = element_list[0].split('Category:')[1].split('Verified team:')[0].replace('\n','')
    df['industy'].loc[i]=industy_element

    whitelist_element = element_list[0].split('Whitelist of investors:')[1].split('KYC of investors:')[0].replace('\n','')
    df['whitelist'].loc[i]=whitelist_element


    KYC_element = element_list[0].split('KYC of investors:')[1].split('Goal of funding (Soft cap):')[0].replace('\n','')
    if KYC_element[:3] == 'Yes':
        df['KYC'].loc[i] = 'Yes'
    else : df['KYC'].loc[i] = 'No'


    if element_list[0] != element_list[0].split('Goal of funding (Soft cap):')[0] :
        soft_element = element_list[0].split('Goal of funding (Soft cap):')[1].split('Goal of funding (Hard cap):')[0].replace('\n','').replace(' ','')
        df['soft_cap'].loc[i]=soft_element

        hard_element = element_list[0].split('Goal of funding (Hard cap):')[1].split('Token price:')[0].split('Tokens for sale:')[0].replace('\n','').replace(' ','')
        df['hard_cap'].loc[i]=hard_element
    else :
        df['soft_cap'].loc[i]= ''
        df['hard_cap'].loc[i]= ''

    if element_list[0] != element_list[0].split('Tokens for sale:')[0] :
        tokensale_element = element_list[0].split('Tokens for sale:')[1].split('Airdropprogram:')[0].split('Token price:')[0].replace('\n','').replace(' ','')
        df['tokens_for_sale'].loc[i] = tokensale_element
    else : df['tokens_for_sale'].loc[i] = ''


    if element_list[0] == element_list[0].split('Token price:')[0] : 
        df['price'].loc[i] = ''
    else :
        price_element = element_list[0].split('Token price:')[1].split('Airdrop program:')[0].split('Minimum purchase:')[0].split('Maximum purchase:')[0].replace('\n','').replace('\t','').split('= ')[1]
        df['price'].loc[i] = price_element


    if element_list[0] == element_list[0].split('Minimum purchase:')[0] :         
        df['min'].loc[i] = ''
    else : 
        min_element = element_list[0].split('Minimum purchase:')[1].split('Airdrop program:')[0].split('Maximum purchase:')[0].replace('\n','').replace(' ','')
        df['min'].loc[i]=min_element

    if element_list[0] == element_list[0].split('Maximum purchase:')[0] : 
        df['max'].loc[i] = ''
    else : 
        max_element = element_list[0].split('Maximum purchase:')[1].split('Airdrop program:')[0].replace('\n','').replace(' ','')
        df['max'].loc[i]=max_element

    bounty_element = element_list[0].split('Bounty program:')[1].split('Have escrow agent:')[0].replace('\n','')
    df['bounty'].loc[i] = bounty_element

    if element_list[0] != element_list[0].split('White paper:')[0] :
        whitepaper_element = element_list[0].split('White paper:')[1].split('Platform:')[0].split('Currencies:')[0].replace('\n','')
        df['whitepaper'].loc[i] = whitepaper_element
    else : df['whitepaper'].loc[i] = ''

    if element_list[0] != element_list[0].split('Currencies:')[0] :
        if element_list[0] == element_list[0].split('Platform:')[0] : 
            if element_list[0] == element_list[0].split('Token type:')[0] :     
                currencies_element = element_list[0].split('Currencies:')[1].split('Location:')[0].split('Exchange markets:')[0].split('Type:')[0].replace('\n','')
                df['currencies'].loc[i] = currencies_element
                df['platform'].loc[i] = ''
                df['token_standard'].loc[i] = ''
            else : 
                currencies_element = element_list[0].split('Currencies:')[1].split('Location:')[0].split('Token type:')[0].replace('\n','')
                df['currencies'].loc[i] = currencies_element
                df['platform'].loc[i] = ''
                token_standard_element = element_list[0].split('Location:')[0].split('Exchange markets:')[0].split('Token type:')[1].split('Type:')[0].replace('\n','')
                df['token_standard'].loc[i] = token_standard_element

        else : 
            if element_list[0] == element_list[0].split('Token type:')[0] :     
                currencies_element = element_list[0].split('Currencies:')[1].split('Location:')[0].split('Exchange markets:')[0].split('Platform:')[0].replace('\n','')
                df['currencies'].loc[i] = currencies_element
                platform_element = element_list[0].split('Platform:')[1].split('Location:')[0].split('Exchange markets:')[0].split('Type:')[0].replace('\n','')
                df['platform'].loc[i] = platform_element
                df['token_standard'].loc[i] = ''
            else : 
                currencies_element = element_list[0].split('Currencies:')[1].split('Location:')[0].split('Exchange markets:')[0].split('Platform:')[0].replace('\n','')
                df['currencies'].loc[i] = currencies_element
                platform_element = element_list[0].split('Platform:')[1].split('Location:')[0].split('Exchange markets:')[0].split('Token type:')[0].replace('\n','')
                df['platform'].loc[i] = platform_element
                token_standard_element = element_list[0].split('Location:')[0].split('Exchange markets:')[0].split('Token type:')[1].split('Type:')[0].replace('\n','')
                df['token_standard'].loc[i] = token_standard_element
    else : df['currencies'].loc[i] = ''

    if len(element_list[0].split('Type:')) == 3 : 
        role_of_token_element = element_list[0].split('Type:')[2].split('Location')[0].split('Exchange markets:')[0].replace('\n','')
        df['role_of_token'].loc[i] = role_of_token_element
    else : df['role_of_token'].loc[i] = ''


    if element_list[0] == element_list[0].split('Restricted areas:')[0] : 
        location_element =  element_list[0].split('Location:')[1].split('Website:')[0].replace('\n','')
        df['location'].loc[i] = location_element
        df['restricted_areas'].loc[i] = 'NO'

    else : 
        location_element =  element_list[0].split('Location:')[1].split('Restricted areas:')[0].replace('\n','')
        df['location'].loc[i] = location_element
        df['restricted_areas'].loc[i] = 'YES'

    if element_list[0] == element_list[0].split('Restricted areas:')[0] : 
        df['location'].loc[i] = location_element
        df['restricted_areas'].loc[i] = 'NO'

    #social_medial
    tags = soup.select('#ico-sum-cont > div > div.col-xs-12.col-sm-12.col-md-7.col-lg-7 > table > tbody')[0].find_all('a')
    element_list = []
    for tag in tags :
        element_list.append(tag.text)
    social_medial_element = 0
    for link in element_list : 
        if link == '' : 
            social_medial_element = social_medial_element + 1
    df['social_medial'].loc[i] = social_medial_element

    #start, end
    tags = soup.select('#ico-start')
    element_list = [0]
    for tag in tags :
        element_list.append(tag.text)
    if len(element_list) == 1 : 
        df['start'].loc[i] == ''
    else : 
        start_element = element_list[1].replace('\n','').replace('\t\t\t\t\t\t\t\t',' ')
        df['start'].loc[i] = start_element

    tags = soup.select('#ico-end')
    element_list = [0]
    for tag in tags :
        element_list.append(tag.text)
    if len(element_list) == 1 : 
        df['end'].loc[i] == ''
    else : 
        end_element = element_list[1].replace('\n','').replace('\t\t\t\t\t\t\t\t',' ')
        df['end'].loc[i] = end_element

    #received
    tags = soup.select('.progress')
    element_list = [0]
    for tag in tags :
        element_list.append(tag.text)
    if len(element_list) == 1 : 
        df['received'].loc[i] == ''
    else : 
        received_element = element_list[1].replace('\n','')
        df['received'].loc[i] = received_element

    
    #bonuses
    tags = soup.select('.ico-subttl')
    for tag in tags :
        element_list.append(tag.text)
    df['bonuses'].loc[i] = 'NO'
    for element in element_list : 
        if element == ' Bonuses and discounts' : 
            df['bonuses'].loc[i] = 'YES'


    #team, advisos
    tags = soup.select('#ico-team-cont')
    df['team'].loc[i] = 0
    df['advisors'].loc[i] = 0
    element_list = [0]
    for tag in tags :
        element_list.append(tag.text)

    if len(element_list) != 1 : 
        if element_list[1] != element_list[1].split('TEAM')[0] :
            team_element = len(element_list[1].split('TEAM')[1].split('ADVISORS')[0].split('\n\n\n\n\n\n\n\n\n\n'))
            df['team'].loc[i] = team_element
        if element_list[1] != element_list[1].split('ADVISORS')[0] :
            advisor_element = len(element_list[1].split('ADVISORS')[1].split('\n\n\n\n\n\n\n\n\n\n'))
            df['advisors'].loc[i] = advisor_element


# df.to_csv('crawling_result3.0.200.csv', encoding='utf-8-sig')
# df.to_csv('crawling_result3.200.400.csv', encoding='utf-8-sig')
# df.to_csv('crawling_result3.400.800.csv', encoding='utf-8-sig')
# df.to_csv('crawling_result3.800.1600.csv', encoding='utf-8-sig')
# df.to_csv('crawling_result3.1600.2200.csv', encoding='utf-8-sig')
# df.to_csv('crawling_result3.2200.2600.csv', encoding='utf-8-sig')
df.to_csv('crawling_result3.final.csv', encoding='utf-8-sig')