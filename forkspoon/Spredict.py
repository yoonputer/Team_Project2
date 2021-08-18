# to_web.py
# -*- coding: utf-8 -*-
# from eunjeon import Mecab
from konlpy.tag import Hannanum
import tensorflow as tf
import sqlite3
import pandas as pd
import numpy as np
import pickle


class Spredict:
    def __init__(self):
        self.connect = sqlite3.connect('db.sqlite3')
        print('1')
        self.stopwords = pd.read_sql_query('select * from stopwords', self.connect)
        print('2')

        self.ko_stopwords_list = np.array(self.stopwords['words'].tolist())
        print('3')

        self.new_model = tf.keras.models.load_model('write/test_dummy_LSTM.h5')
        print('4')


        with open('write/tokenizers.pkl', 'rb') as f:
            self.tokenizer = pickle.load(f)

    def sentance_predict(self, sentence):
        mecab = Hannanum()
        input_sentance = mecab.morphs(sentence)
        input_sentance = [tok for tok in input_sentance if tok not in self.ko_stopwords_list]
        encoded = self.tokenizer.texts_to_sequences([input_sentance])
        pad_new = tf.keras.preprocessing.sequence.pad_sequences(encoded, maxlen=300)
        score = self.new_model.predict(pad_new)
        return [score, np.argmax(score)]


# sentencess = '탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락탈락'

# print(sentance_predict(sentencess))
# print(np.argmax(sentance_predict(sentencess)))
