import pickle
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

urllist= pickle.load(open('./urllist.pkl','rb'))
# print(len(urllist)) #2475
group = []

for i in urllist[:2475]:
    try:
        data = requests.get(i)
        soup = BeautifulSoup(data.content, "html.parser")

        contents = soup.select('section#user-container')[0]

        for u in data:
            title = contents.select('div.article-head-title')[0].text.strip()
            article = contents.select('div#article-view-content-div')[0].text.strip()

        group.append([title, article])
    except IndexError:
        pass

try:
#     result = group
    df2 = pd.DataFrame(group, columns=['title','content']) #라벨링
    print(df2)
except TypeError as e: # none값 제거
    print('제거함')

pickle.dump(df2,open('./df2.pkl','wb'))