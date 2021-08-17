from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://obank.kbstar.com/quics?page=C016613')
time.sleep(3)