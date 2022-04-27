from functools import total_ordering
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
from selenium.webdriver import ActionChains

load_dotenv()
total_df = pd.DataFrame()
review_df = pd.DataFrame(columns = ['review','taste','quantity','delivery','total'])
driver = webdriver.Chrome(os.environ.get("CHROME_DRIVER"))
#driver = webdriver.Chrome('C:/Users/kkakkuro0/Desktop/seoultech/programing/crawling/chromedriver')
driver.get('https://www.yogiyo.co.kr/mobile/#/')

driver.find_element_by_xpath('//*[@id="search"]/div/form/input').click()
driver.find_element_by_xpath('//*[@id="search"]/div/form/ul/li[1]').click()
driver.implicitly_wait(3)
driver.execute_script("window.scrollTo(0, 100000)")

driver.find_element_by_xpath(f'//*[@id="content"]/div/div[4]/div/div[2]/div[30]').click()
element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a')
driver.execute_script("arguments[0].click();", element)

review = driver.find_element_by_xpath('//*[@id="review"]/li[2]/p').text

star_taste = int(driver.find_element_by_xpath('//*[@id="review"]/li[2]/div[2]/div/span[2]/span[3]').text)

star_quantity = int(driver.find_element_by_xpath('//*[@id="review"]/li[2]/div[2]/div/span[2]/span[6]').text)
star_delivery = int(driver.find_element_by_xpath('//*[@id="review"]/li[2]/div[2]/div/span[2]/span[9]').text)

star_total = floor(mean([star_taste,star_quantity,star_delivery]))
review_df = pd.DataFrame({'review':[review],'taste':[star_taste],'quantity':[star_quantity],'delivery':[star_delivery],'total':[star_total]})
print(review_df)
total_df = pd.concat([total_df,review_df])
print(total_df)
