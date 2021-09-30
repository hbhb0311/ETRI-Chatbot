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

driver.get(url)
time.sleep(3)
idx = 0

for i in range(1, 3):
    for j in range(1, 6):
        if i == 1 and j == 5:
            continue
        button = driver.find_element_by_xpath(f'//*[@id="b061574"]/ul[{i}]/li[{j}]/a')
        button.click()

        text = driver.page_source
        soup = BeautifulSoup(text, 'html.parser')
        tag = soup.find_all('div', class_ = 'area1')

        for t in tag:
            print(t.a.strong.get_text())
            onclickspt = t.a['onclick'].split(',')
            df.loc[idx, '상품명'] = t.a.strong.get_text()
            df.loc[idx, '가입목적'] = onclickspt[3]
            url_add = onclickspt[0][-11: -1]
            print(f'{url}&cc=b061574:b032054&prcode={url_add}')
            break
            driver.get(f'{url}&cc=b061574:b032054&prcode={url_add}')
            text = driver.page_source
            soup = BeautifulSoup(text, 'html.parser')
            print(soup)
            break
            tag_prod = soup.find_all('ul', class_ = 'n_productInfo')
            print(tag_prod)

            for tp in tag_prod:
                break


# dtlBanka('BK09000261','0','0','펀드/외화투자', '적립식', '변동금리', '저축성보험', 'N');