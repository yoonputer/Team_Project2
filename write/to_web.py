from konlpy.tag import Mecab
import tensorflow as tf
import sqlite3
import pandas as pd
import numpy as np
import pickle

connect = sqlite3.connect('../db.sqlite3')
stopwords = pd.read_sql_query('select * from stopwords',connect)
ko_stopwords_list = np.array(stopwords['words'].tolist())
new_model = tf.keras.models.load_model('../../Deeplearning/test_dummy_LSTM.h5')

with open('../../Deeplearning/tokenizers.pkl','rb') as f:
    tokenizer = pickle.load(f)

def sentance_predict(sentence):
    mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
    input_sentance = mecab.morphs(sentence)
    input_sentance = [tok for tok in input_sentance if tok not in ko_stopwords_list]
    encoded = tokenizer.texts_to_sequences([input_sentance])
    pad_new = tf.keras.preprocessing.sequence.pad_sequences(encoded, maxlen=300)
    score = new_model.predict(pad_new)
    return score


sentencess = '성실합니다'
print(sentance_predict(sentencess))
print(np.argmax(sentance_predict(sentencess)))