from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.alert import Alert

yegeum = ['categoryD00169', 'categoryD00027', 'categoryD00031', 'categoryD00025']
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://obank.kbstar.com/quics?page=C016613#CP')
time.sleep(3)

for i in yegeum:
    driver.execute_script("document.getElementById('layer_today_0819').style.display='none';")
    driver.execute_script("document.getElementById('uiNavSnb').style.display='none';")
    button = driver.find_element_by_class_name(f'tabMenu #{i}')
    button.click()

    time.sleep(3)

    text = driver.page_source
    soup = BeautifulSoup(text, 'html.parser')
    tag = soup.find_all('div', class_='area1')
    url = 'https://obank.kbstar.com/quics?page=C016613'
    aa = soup.find_all('form', action = '/quics?page=C016613&CC=b061496:b061496')

    for k in aa:
        button = driver.find_element_by_class_name(f"paging #{k['id']}")
        button.click()
        time.sleep(3)
        text = driver.page_source
        soup = BeautifulSoup(text, 'html.parser')
        tag = soup.find_all('div', class_='area1')

        for t in tag:
            print(t.a.strong.get_text())
            urldp = t.a['onclick'][12:22]
            url_ = f'{url}&cc=b061496:b061645&isNew=N&prcode={urldp}'
            ress = requests.get(url_)

            soupp = BeautifulSoup(ress.text, features="html.parser")

            try:
                tagg = soupp.find('div', id='uiProTabCon1')

                for i in tagg.find_all('tr'):
                    print(i.th.get_text())
                    for j in i.find_all('td'):
                        print(j.get_text())

            except:
                print('!!!!!!!!!!!오류 발생')

            print('-----------------------------------------------------')



# driver.get('https://obank.kbstar.com/quics?page=C019478')
# time.sleep(3)
# button = driver.find_element_by_class_name('tabMenu #tab_menu2')
# button.click()
# time.sleep(3)
