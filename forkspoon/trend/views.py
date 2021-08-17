from django.shortcuts import render

# Create your views here.


def trendview(request):
    return render(request, 'trend/trend.html')


from konlpy.tag import Mecab
def sentiment_predict(sentence):
  mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
  new_sentence = okt.morphs(sentence)
  new_sentence = [ tok for tok in new_sentence if tok not in stopwords ]
  encoded = tokenizer.texts_to_sequences([new_sentence])
  pad_new = tf.keras.preprocessing.sequence.pad_sequences(encoded, maxlen=50)
  score = loaded_model.predict(pad_new)
  return score

import tensorflow as tf
def test_dummy_h5(score):
    model = tf.keras.models.load_model('./Deeplearning/test_dummy_LSTM.h5')
    result = model.predict([sentiment_predict(sentence)])
    return result



