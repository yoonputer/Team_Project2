import sqlite3
import pandas as pd
connect = sqlite3.connect('../forkspoon/db.sqlite3')
choice = pd.read_sql_query('select * from write_choice',connect)
choice_cols = choice[['점수','질문','답변']]
# print(choice_cols)

from sklearn.model_selection import train_test_split
x_data = choice_cols['답변']
y_data = choice_cols['점수']
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)
# print(x_train.shape, y_train.shape,x_test.shape, y_test.shape)
# (2247,) (2247,) (750,) (750,)

x_temp = x_train
x_temp= x_temp.str.replace('[^가-힣ㄱ-ㅎ0-9ㅏ-ㅣ]','')
# print(x_temp) # Name: 답변, Length: 2247, dtype: object

stopwords = pd.read_sql_query('select * from stopwords',connect)
# print(stopwords.describe())
#        words
# count   1543
# unique   567
# top        하
# freq      90

import numpy as np
ko_stopwords_list = np.array(stopwords['words'].tolist())
# print(ko_stopwords_list)
# ['이' '있' '하' ... '잘' '통하' '놓']

from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")

# mecab.pos(x_temp[0])
# mecab.morphs(x_temp[0])

def non_stopwords(x_temp):
    sentance = list()
    for tok in x_temp:
        encoded = mecab.morphs(tok)
        sentance.append([item for item in encoded if item not in ko_stopwords_list])
    return sentance
print(non_stopwords(x_temp[0]))
#
# import tensorflow as tf
# tokenizer = tf.keras.preprocessing.text.Tokenizer()
# tokenizer.fit_on_texts(non_stopwords(x_temp))
# # print(tokenizer.word_index)
# # print(tokenizer.word_counts)
# total_cnt = len(tokenizer.word_index)
# rare_cnt = 0
# total_freq,rare_freq = 0,0
# for key, value in tokenizer.word_counts.items():
#   total_freq = total_freq + value #전체 단어의 수
#   if(value <=2):
#     rare_cnt = rare_cnt+ 1
#     rare_freq = rare_freq + value #2미만인 단어(희귀단어)의 수
# print(total_cnt, rare_cnt, (rare_cnt/total_cnt)*100, (rare_freq/total_freq)*100)
# vocab_size = total_cnt - rare_cnt #보케블러리 사이즈
# # print(vocab_size)
#
# tokenizer = tf.keras.preprocessing.text.Tokenizer(vocab_size, oov_token='OOV')
# tokenizer.fit_on_texts(non_stopwords(x_temp))
# # print(tokenizer.index_word)
#
# x_train = tokenizer.texts_to_sequences(non_stopwords(x_temp))
# print(len(x_train[0]),len(x_train[40]),len(x_train[50]))
#
# hist_len = [len(words) for words in x_train]
# print(sum(hist_len)/ len(x_train))
# x_train =tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=350)
#
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Embedding(input_dim= vocab_size, output_dim =30 ,input_length=350))
# model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(128)))
# model.add(tf.keras.layers.Dense(8,activation='softmax'))
# model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['acc'])
#
# hist = model.fit(x_train, y_train, epochs=100, batch_size=256, validation_split=0.3, shuffle=True)
#
# print(model.evaluate(x_train, y_train))
