from multiprocessing.dummy import Pool as ThreadPool
import requests
from bs4 import BeautifulSoup
import pandas as pd


def parming(myurl):
    try:
        mylist = []
        뉴데이터 = requests.get(myurl)
        soup = BeautifulSoup(뉴데이터.content, "html.parser")

        제목 = soup.select_one('div.viewTitWrap > h2.hd > strong').text
        점수 = soup.select_one('.grade').text
        질문 = soup.select('dt.on')
        답변 = soup.select('dd.show')

        for idx, val in enumerate(답변):
            if '선택한' in val.text:
                mylist = [제목.strip(), 점수.strip(),val.text,답변[idx].text]
                break
        return mylist
    except AttributeError as e:
        print(myurl+" = 별점없음")


url = 'https://www.jobkorea.co.kr'
urllist = []

# 데이터 = requests.get(
#     'https://www.jobkorea.co.kr/starter/passassay?schTxt=%EC%84%A0%ED%83%9D%ED%95%9C&Page=1')

# 잡코리아의 자소서 페이지의 주소 추출하기
for i in range(1, 175):
    makingurl = f'https://www.jobkorea.co.kr/starter/PassAssay?FavorCo_Stat=0&Pass_An_Stat=0&OrderBy=2&EduType=0&WorkType=0&isSaved=0&Page={i}'
    데이터 = requests.get(makingurl)

    soup = BeautifulSoup(데이터.content, "html.parser")
    link1 = soup.find_all('a', class_="logo")
    for j in range(len(link1)):
        urllist.append(url+link1[j]['href'])

print(urllist)  # 주석처리 하셔도됨


# 추출한 주소를 토대로 자소서 질답 추출하기


pool = ThreadPool(16)
result = pool.map(parming, urllist)
pool.close()
pool.join()

print(result)
result = list(filter(None, result))

try:
    a = pd.DataFrame(result, columns=['제목','점수','질문','답변'])
except TypeError as e:
    print('pass')

print(a)
# 엑셀로 저장 하려면 터미널에서 pip install openpyxl 해주세요

a.to_excel("alldata.xlsx", index=False)