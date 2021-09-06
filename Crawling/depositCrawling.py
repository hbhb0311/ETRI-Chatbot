from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


# catlst = ['C016613', 'C103429', 'C016567', 'C019503', 'C016622', 'C101501']
df = pd.DataFrame()
deposit = ['categoryD00169', 'categoryD00027', 'categoryD00031', 'categoryD00025']

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://obank.kbstar.com/quics?page=C016613#CP')
time.sleep(3)

idx = 0
for i in deposit:
    driver.execute_script("document.getElementById('layer_today_0819').style.display='none';")
    driver.execute_script("document.getElementById('uiNavSnb').style.display='none';")
    button = driver.find_element_by_class_name(f'tabMenu #{i}')
    button.click()

    time.sleep(3)

    text = driver.page_source
    soup = BeautifulSoup(text, 'html.parser')
    tag = soup.find_all('div', class_='area1')
    url = 'https://obank.kbstar.com/quics?page=C016613'
    page = soup.find_all('form', action = '/quics?page=C016613&CC=b061496:b061496')

    for k in page:
        button = driver.find_element_by_class_name(f"paging #{k['id']}")
        button.click()
        time.sleep(3)
        text = driver.page_source
        soup = BeautifulSoup(text, 'html.parser')
        tag = soup.find_all('div', class_='area1')

        for t in tag:
            print(t.a.strong.get_text())
            df.loc[idx, '상품명'] = t.a.strong.get_text()
            urldp = t.a['onclick'][12:22]
            url_ = f'{url}&cc=b061496:b061645&isNew=N&prcode={urldp}'
            ress = requests.get(url_)

            soupp = BeautifulSoup(ress.text, features="html.parser")
            tagg = soupp.find('div', id='uiProTabCon1')

            try:
                if tagg.find_all('tr')[0].th.get_text() != '구   분':
                    for i in tagg.find_all('tr'):
                        colname = i.th.get_text().strip().replace('\n', '')
                        df.loc[idx, colname] = ''

                        for j in i.find_all('td'):
                            jtext = j.get_text().strip().replace('\n', '')
                            if 'X' in jtext:
                                jtext = '불가능'
                            elif 'O' in jtext:
                                jtext = '가능'
                            df.loc[idx, colname] += jtext
                else:
                    tagg = soupp.find('div', class_ = 'infoCont')
                    tagg = tagg.find('tbody')
                    for i in tagg.find_all('tr'):
                        colname = i.td.get_text().strip().replace('\n', '')
                        df.loc[idx, colname] = ''

                        for j in i.find_all('td'):
                            jtext = j.get_text().strip().replace('\n', '')
                            if jtext == colname:
                                continue
                            if 'X' in jtext:
                                jtext = '불가능'
                            elif 'O' in jtext:
                                jtext = '가능'
                            df.loc[idx, colname] += jtext
            except:
                print('오류발생!!')

            idx += 1
            print(df)
            print('-----------------------------------------------------')

df.to_csv('deposit.csv', index = False)