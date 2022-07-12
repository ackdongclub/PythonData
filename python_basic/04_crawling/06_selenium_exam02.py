from selenium import webdriver
import os,time
path = os.path.dirname(__file__)
dirver =  webdriver.Chrome(path+'/dirver/chromedriver')
driver.implicitly_wait(15)

driver.fullscreen_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
drive.maximize_window()
time.sleep()
driver.set_window_rect(100, 100)