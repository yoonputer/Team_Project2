import sqlite3
import pickle
import pandas as pd

''' 피클 불러오기
data_pkl= pickle.load(open('groups.pkl', 'rb'))
print(data_pkl)
'''

''' 피클-> 데이터프레임 담기
data_df= pd.DataFrame(data_pkl)
print(data_df)
'''

''' 디비 -> 데이터프레임 불러오기
connect = sqlite3.connect('../../forkspoon/db.sqlite3')
data_df.to_sql('groups',connect, if_exists='replace')
df = pd.read_sql_query('select * from groups',connect)
print(df)
'''

''' 데이터프레임 -> 엑셀로 저장
df.to_excel('./group_data.xls')
'''

''' Okt 테스트
from konlpy.tag import Okt
txt = "아버지가방에들어가신다."
okt = Okt()

sentence = okt.morphs(txt)
print(sentence)
#python -m pip install JPype1==1.2.0
'''