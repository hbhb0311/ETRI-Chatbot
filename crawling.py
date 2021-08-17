import requests
from bs4 import BeautifulSoup
import xmltodict, json

url = 'https://obank.kbstar.com/quics?page=C016613'
res = requests.get(url)

soup = BeautifulSoup(res.text, features="html.parser")
tag = soup.find_all('div', class_ = 'area1')


################################################
# urldp = tag.a['onclick'][12:22]
# url_ = f'{url}&cc=b061496:b061645&isNew=N&prcode={urldp}'
#
# ress = requests.get(url_)
# soupp = BeautifulSoup(ress.text, features="html.parser")
# tag = soupp.find('div', id = 'uiProTabCon1')
# # print(tag.find_all('tr'))
#
# for i in tag.find_all('tr'):
#     print(i.th.get_text())
#     for j in i.find_all('td'):
#         print(j.get_text())

for t in tag:
    print(t.a.strong.get_text())
    urldp = t.a['onclick'][12:22]
    url_ = f'{url}&cc=b061496:b061645&isNew=N&prcode={urldp}'
    ress = requests.get(url_)

    soupp = BeautifulSoup(ress.text, features="html.parser")

    try:
        tagg = soupp.find('div', id = 'uiProTabCon1')

        for i in tagg.find_all('tr'):
            print(i.th.get_text())
            for j in i.find_all('td'):
                print(j.get_text())

    except:
        print('!!!!!!!!!!!오류 발생')

    print('-----------------------------------------------------')
