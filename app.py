import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.jobkorea.co.kr'
urllist = []

# 데이터 = requests.get(
#     'https://www.jobkorea.co.kr/starter/passassay?schTxt=%EC%84%A0%ED%83%9D%ED%95%9C&Page=1')

# 잡코리아의 자소서 페이지의 주소 추출하기
for i in range(1, 2):
    makingurl = f'https://www.jobkorea.co.kr/starter/passassay?schTxt=%EC%84%A0%ED%83%9D%ED%95%9C&Page={i}'
    데이터 = requests.get(makingurl)

    soup = BeautifulSoup(데이터.content, "html.parser")
    link1 = soup.find_all('a', class_="logo")
    for j in range(len(link1)):
        urllist.append(url+link1[j]['href'])

print(urllist)  # 주석처리 하셔도됨

# 추출한 주소를 토대로 자소서 질답 추출하기
질문리스트 = []
for i in range(len(urllist)):
    뉴데이터 = requests.get(urllist[i])
    soup = BeautifulSoup(뉴데이터.content, "html.parser")

    제목 = soup.select_one('div.viewTitWrap > h2.hd > strong').text
    점수 = soup.select_one('.grade').text
    질문 = soup.select('dl.qnaLists > dt >button > span.tx')
    답변 = soup.select('dl.qnaLists > dd > div.tx')

    for idx, val in enumerate(질문):
        if '선택한' in val.text:
            질문리스트.append([제목.strip(), 점수.strip(), val.text, 답변[idx].text])
            break

# 리턴되는 질문리스트는 리스트 타입이고 [ [질문, 답변] ,[질문, 답변] ,[질문, 답변] ,...] 형태로 '선택한'이 들어간 질문만 찾아서 해당 답변을 리턴합니다. 데이터프레임으로 옮겨서 엑셀저장 만 하시면 됩니다. , 한글 그대로 쓰셔도 됩니다.
# print(질문리스트)  # 주석처리 하셔도됨
# 데이터프레임으로 저장
a = pd.DataFrame(질문리스트, columns=['제목', '점수', '질문', '답변'])
print(a)
# 엑셀로 저장 하려면 터미널에서 pip install openpyxl 해주세요
a.to_excel("projectdata.xlsx", index=False)

