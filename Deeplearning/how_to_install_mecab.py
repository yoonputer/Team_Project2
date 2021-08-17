##### 파이참에 mecab 설치하기 #####

# Mecab 설치나 사용은 다음의 2 사이트 참조
# https://joyhong.tistory.com/127
# https://hong-yp-ml-records.tistory.com/91
# 설치 할땐 첫번째 사이트, 사용법을 볼 땐 두번째 사이트 이용을 추천
# 별개로 위의 설치과정중엔 없지만 python interpreter쪽에 konlpy의 설치가 필요
# 그 외 참조하면 좋은 곳
# https://m.blog.naver.com/PostView.nhn?blogId=aul-_-&logNo=221557243190&proxyReferer=https:%2F%2Fwww.google.com%2F



# 아래의 코드는 설치과정중에 Python Console에서 입력해야 하는 코드들 ( 사이트에서 복사시 자동으로 출처가 붙음 )

import pip
from pip._internal import main as pipmain
def install_whl(path):
    pipmain(['install', path])

install_whl('C:/mecab/mecab_python-0.996_ko_0.9.2_msvc-cp36-cp36m-win_amd64.whl')


# django에서 mecab쓸 때
# mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")


