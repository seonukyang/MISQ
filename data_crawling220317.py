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

dict = {'year':[],'volumn':[],'season':[],'table':[],'url':[], 'keyword':[]}
df = pd.DataFrame(dict) 

for volume in range(1,46,1) : 
    for season in range(1,5,1) : 
        if volume < 10 : 
            volume_text = '0'+str(volume)
        print('volume = ', volume)
        print('season = ',season)

        url_base = 'https://misq.umn.edu/contents-'+str(volume_text)+'-'+str(season)
        req = urllib.request.Request(url_base, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = bs(html, 'html.parser')
    
        tags = soup.select('#maincontent > div.columns > div')
        table_list =  str(tags).split('a href=')
 
        for table_num in range(1, len(table_list),1) :     
            url_target = table_list[table_num].split('"')[1]
            req = urllib.request.Request(url_target, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(req).read()
            soup = bs(html, 'html.parser')
            print(soup)
            keywords = soup.select('#maincontent > div.columns > div > div.additional > div.content > div > table > tbody')
            # print(keywords)
