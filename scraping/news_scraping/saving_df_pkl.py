import sqlite3
import pickle
import pandas as pd

# data_pkl= pickle.load(open('groups.pkl', 'rb'))
# print(data_pkl)

# data_df= pd.DataFrame(data_pkl)
# print(data_df)

connect = sqlite3.connect('../../forkspoon/db.sqlite3')
# data_df.to_sql('groups',connect, if_exists='replace')
df = pd.read_sql_query('select * from groups',connect)
print(df)

df.to_excel('./group_data.xls')