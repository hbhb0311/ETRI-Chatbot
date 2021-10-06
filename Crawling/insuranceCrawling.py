from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

df = pd.DataFrame()

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
url = 'https://obank.kbstar.com/quics?page=C019503'
url_ins = f'{url}&cc=b061574:b032054&prcode='

idx = 0

for i in range(1, 3):
    driver.get(url)
    time.sleep(3)

    for j in range(1, 6):
        if i == 1 and j == 4:
            continue

        button = driver.find_element_by_xpath(f'//*[@id="b061574"]/ul[{i}]/li[{j}]/a')
        button.click()
        time.sleep(3)

        text = driver.page_source
        soup = BeautifulSoup(text, 'html.parser')
        pages = soup.find_all('form', action = '/quics?page=C019503&CC=b061574:b061574')

        for p in pages:
            button_p = driver.find_element_by_id(p['id'])
            button_p.click()
            time.sleep(2)

            text = driver.page_source
            soup = BeautifulSoup(text, 'html.parser')
            tag = soup.find_all('div', class_ = 'area1')

            for t in tag:
                print(t.a.strong.get_text())
                onclickspt = t.a['onclick'].split(',')
                df.loc[idx, '상품명'] = t.a.strong.get_text()
                df.loc[idx, '가입목적'] = onclickspt[3]
                url_add = onclickspt[0][-11: -1]
                driver.get(f'{url}&cc=b061574:b032054&prcode={url_add}')
                time.sleep(3)
                text = driver.page_source
                soup = BeautifulSoup(text, 'html.parser')
                tag_prod = soup.find_all('ul', class_='n_productInfo')

                for tp in tag_prod:
                    for l in tp.find_all('li'):
                        colname = l.strong.get_text().strip()
                        text = l.div.get_text().strip()
                        df.loc[idx, colname] = text
                idx += 1
            driver.get(url)
            time.sleep(3)

            button = driver.find_element_by_xpath(f'//*[@id="b061574"]/ul[{i}]/li[{j}]/a')
            button.click()
            time.sleep(3)

        df.to_csv('insurance.csv', index=False)
        print(df)
df.to_csv('insurance.csv', index = False)