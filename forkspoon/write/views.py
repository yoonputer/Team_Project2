from django.shortcuts import render, redirect
from Spredict import Spredict  # 딥러닝 파일
from wordc import mkwdcrd  # 딥러닝 파일

# to_web.py
# -*- coding: utf-8 -*-
# from eunjeon import Mecab
# # from konlpy.tag import Mecab
# import tensorflow as tf
# import sqlite3
# import pandas as pd
# import numpy as np
# import pickle


# class Spredict:
#     def __init__(self):
#         self.connect = sqlite3.connect('db.sqlite3')
#         self.stopwords = pd.read_sql_query(
#             'select * from stopwords', self.connect)
#         self.ko_stopwords_list = np.array(self.stopwords['words'].tolist())
#         self.new_model = tf.keras.models.load_model('write/test_dummy_LSTM.h5')

#         with open('write/tokenizers.pkl', 'rb') as f:
#             self.tokenizer = pickle.load(f)

#     def sentance_predict(self, sentence):
#         mecab = Mecab()
#         input_sentance = mecab.morphs(sentence)
#         input_sentance = [
#             tok for tok in input_sentance if tok not in self.ko_stopwords_list]
#         encoded = self.tokenizer.texts_to_sequences([input_sentance])
#         pad_new = tf.keras.preprocessing.sequence.pad_sequences(
#             encoded, maxlen=300)
#         score = self.new_model.predict(pad_new)
#         return [score, np.argmax(score)]


# Create your views here.


def writeview(request):
    if request.method == 'POST':
        contents = request.POST['contents']
        myemail = request.POST['emailtab']
        predict_content = Spredict()
        result = predict_content.sentance_predict(contents)
        # 사이트에서 나의 자소서를 가져옴
        context = {'score': '너의점수는 : ' +
                   str(result[1]), 'myemail': 'write/'+myemail+'.png'}
        mkwdcrd(contents, myemail)
        return render(request, 'write/result.html', context)
    else:
        return render(request, 'write/write.html')
