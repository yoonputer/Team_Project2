# 파이참에 mecab설치

import pip
from pip._internal import main as pipmain
def install_whl(path):
    pipmain(['install', path])
    install_whl('C:/mecab/mecab_python-0.996_ko_0.9.2_msvc-cp36-cp36m-win_amd64.whl')

import MeCab
m = MeCab.Tagger()
a = m.parse("오늘은 좋은날, 행복한 삶을 누리자.")
print(a)

