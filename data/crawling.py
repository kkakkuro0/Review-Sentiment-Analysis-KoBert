import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

review_df = pd.DataFrame()

driver = webdriver.Chrome('C:/Users/kkakkuro0/Desktop/seoultech/programing/crawling/chromedriver')
driver.get('https://www.yogiyo.co.kr/mobile/#/')

driver.find_element_by_xpath('//*[@id="search"]/div/form/input').click()
driver.find_element_by_xpath('//*[@id="search"]/div/form/ul/li[1]').click()
driver.implicitly_wait(3)

review_list = []
for i in range(1,102):
    try:
        driver.find_element_by_xpath(f'//*[@id="content"]/div/div[4]/div/div[2]/div[{i}]').click()
        element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a')
        driver.execute_script("arguments[0].click();", element)
        
        for j in range(2,103):
            try:
                try:
                    review = driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/p').text
                    review_list.append(review)
                except:
                    driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/a').click()
                    review = driver.find_element_by_xpath(f'//*[@id="review"]/li[{j}]/p').text
                    review_list.append(review)     
            except:
                break
    except:
        break

    driver.back()

review_df = pd.DataFrame(review_list, columns = ['review'])
review_df.to_csv('review.csv',index=False,encoding='utf-8-sig')
