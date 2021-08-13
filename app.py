import requests
from bs4 import BeautifulSoup

url = 'https://www.jobkorea.co.kr'
urllist = []

# 데이터 = requests.get(
#     'https://www.jobkorea.co.kr/starter/passassay?schTxt=%EC%84%A0%ED%83%9D%ED%95%9C&Page=1')

for i in range(1, 30):
    makingurl = f'https://www.jobkorea.co.kr/starter/passassay?schTxt=%EC%84%A0%ED%83%9D%ED%95%9C&Page={i}'
    데이터 = requests.get(makingurl)

    soup = BeautifulSoup(데이터.content, "html.parser")
    link1 = soup.find_all('a', class_="logo")
    for j in range(len(link1)):
        urllist.append(url+link1[j]['href'])

질문리스트 = []
for i in range(len(urllist)):
    뉴데이터 = requests.get(urllist[i])
    soup = BeautifulSoup(뉴데이터.content, "html.parser")

    제목 = soup.select_one('div.viewTitWrap > h2.hd > strong').text

    질문 = soup.select('dl.qnaLists > dt >button > span.tx')
    답변 = soup.select('dl.qnaLists > dd > div.tx')

    for idx, val in enumerate(질문):
        if '선택한' in val.text:
            질문리스트.append([val.text, 답변[idx].text])


print(질문리스트)
