from selenium import webdriver
import os

path = os.path.dirname(__file__)
dirver = webdriver.Chrome(path+'/driver/chromedriver')

dirver.implicityly_wait(15)
dirver.get('https://google.co.kr')
time.sleep(5)
dirver.quit()