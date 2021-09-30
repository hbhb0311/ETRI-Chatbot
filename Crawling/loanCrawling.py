from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

df = pd.DataFrame()

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
url = 'https://obank.kbstar.com/quics?page=C103429'
url_loan = f'{url}&cc=b104363:b104516&isNew=N&prcode='
# driver.get(url)
# time.sleep(3)
idx = 0

for i in range(1, 7):
    driver.get(url)
    time.sleep(3)
    # driver.execute_script("document.getElementById('layer_today_0819').style.display='none';")
    # driver.execute_script("document.getElementById('uiNavSnb').style.display='none';")
    if i == 5:
        continue
    button = driver.find_element_by_id(f'tab_menu{i}')
    button.click()

    time.sleep(3)

    text = driver.page_source
    soup = BeautifulSoup(text, 'html.parser')
    # tag = soup.find_all('div', class_='area1')
    page = soup.find_all('form', action = '/quics?page=C103429&CC=b104363:b104363')
    page_idx = 0

    for _ in page:
        page_idx += 1
        button = driver.find_element_by_id(f"pageinput{page_idx}")
        button.click()
        time.sleep(3)
        #
        # text = driver.page_source
        # soup = BeautifulSoup(text, 'html.parser')
        # tag = soup.find_all('div', class_='area1')

        # for t in tag:
        #     print(t.a.strong.get_text())
        #     df.loc[idx, '상품명'] = t.a.strong.get_text()
        #     urlln = t.a['onclick'][9:19]
        #     url_ = f'{url_loan}{urlln}&QSL=F'
        #     ress = requests.get(url_)

        for j in range(1, 11):
            bttn = driver.find_element_by_xpath(f'//*[@id="b104363"]/div[2]/ul[2]/li[{j}]/div[1]/a')
            bttn.click()
            time.sleep(3)

            text = driver.page_source
            soup = BeautifulSoup(text, 'html.parser')
            tag = soup.find('h2', class_='headline')
            print(tag.b.get_text())

            text = driver.page_source
            soup = BeautifulSoup(text, 'html.parser')

            for k in range(1, 3):
                tagg = soup.find('div', id = f'areaBox{k}')

                for t in tagg.ul.find_all('li'):
                    try:
                        colname = t.strong.get_text().replace('\n', '')
                        df.loc[idx, colname] = ''

                        for text in t.div.ul.find_all('li'):
                            txt = text.get_text().strip().replace('\n', '')
                            df.loc[idx, colname] += (txt + ' ')
                    except:
                        print('오류 발생!!!!!!!!!!!!')

            driver.get(url)
            button = driver.find_element_by_id(f'tab_menu{i}')
            button.click()
            button = driver.find_element_by_id(f"pageinput{page_idx}")
            button.click()
            time.sleep(3)

            idx += 1
            print(df)
#            df.to_csv('loan.csv', index=False)
            print('-----------------------------------------------------')

            # try:
            #     if tagg.find_all('tr')[0].th.get_text() != '구   분':
            #         for i in tagg.find_all('tr'):
            #             colname = i.th.get_text().strip().replace('\n', '')
            #             df.loc[idx, colname] = ''
            #
            #             for j in i.find_all('td'):
            #                 jtext = j.get_text().strip().replace('\n', '')
            #                 if 'X' in jtext:
            #                     jtext = '불가능'
            #                 elif 'O' in jtext:
            #                     jtext = '가능'
            #                 df.loc[idx, colname] += jtext
            #     else:
            #         tagg = soupp.find('div', class_ = 'infoCont')
            #         tagg = tagg.find('tbody')
            #         for i in tagg.find_all('tr'):
            #             colname = i.td.get_text().strip().replace('\n', '')
            #             df.loc[idx, colname] = ''
            #
            #             for j in i.find_all('td'):
            #                 jtext = j.get_text().strip().replace('\n', '')
            #                 if jtext == colname:
            #                     continue
            #                 if 'X' in jtext:
            #                     jtext = '불가능'
            #                 elif 'O' in jtext:
            #                     jtext = '가능'
            #                 df.loc[idx, colname] += jtext
            # except:
            #     print('오류발생!!')

df.to_csv('loan.csv', index = False)