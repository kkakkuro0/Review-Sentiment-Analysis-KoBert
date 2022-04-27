from math import floor
from statistics import mean
from numpy import int0
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import numpy as pd

load_dotenv()
total_df = pd.DataFrame()
driver = webdriver.Chrome(os.environ.get("CHROME_DRIVER"))
#driver = webdriver.Chrome('C:/Users/kkakkuro0/Desktop/seoultech/programing/crawling/chromedriver')
driver.get('https://www.yogiyo.co.kr/mobile/#/')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="search"]/div/form/input').click()
driver.find_element_by_xpath('//*[@id="search"]/div/form/ul/li[1]').click()
driver.implicitly_wait(3)

review_list = []
for i in range(1,102):
    try:
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(f'//*[@id="content"]/div/div[4]/div/div[2]/div[{i}]').click()
        element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a')
        driver.execute_script("arguments[0].click();", element)
        
        for j in range(2,103):
            try:
                try:
                    driver.implicitly_wait(10)
                    review = driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/p').text
                    star_taste = int(driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/div[2]/div/span[2]/span[3]').text)
                    star_quantity = int(driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/div[2]/div/span[2]/span[6]').text)
                    star_delivery = int(driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/div[2]/div/span[2]/span[9]').text)
                    star_total = floor(mean([star_taste,star_quantity,star_delivery]))
                    review_df = pd.DataFrame({'review':[review],'taste':[star_taste],'quantity':[star_quantity],'delivery':[star_delivery],'total':[star_total]})
                    total_df = pd.concat([total_df,review_df])
                except:
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/a').click()
                    review = driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/p').text
                    star_taste = int(driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/div[2]/div/span[2]/span[3]').text)
                    star_quantity = int(driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/div[2]/div/span[2]/span[6]').text)
                    star_delivery = int(driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/div[2]/div/span[2]/span[9]').text)
                    star_total = floor(mean([star_taste,star_quantity,star_delivery]))
                    review_df = pd.DataFrame({'review':[review],'taste':[star_taste],'quantity':[star_quantity],'delivery':[star_delivery],'total':[star_total]})
                    total_df = pd.concat([total_df,review_df])
            except:
                break
        print(f'({i}/100) complete')
    except:
        break

    driver.back()
#print(total_df)
#review_df = pd.DataFrame(review_list, columns = ['review','taste','quantity','delivery','total'])
total_df.to_csv('review_new.csv',index=False,encoding='utf-8-sig')
