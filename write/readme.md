#### ➺<a href="https://github.com/yoonputer/Team_Project2">  home </a>

# <a href="https://github.com/yoonputer/Team_Project2">  Web-server </a>  by 김도관


![화면 캡처 2021-08-20 135731](https://user-images.githubusercontent.com/83646543/130181892-cdbd29b5-7c76-4f37-a922-ff7cd08ec4a9.jpg)

전체적인 구성 설명

* Main service 는 앞서 학습한 모델을 사용하기 위한 페이지의 write앱 의 view파일은 

  클라이언트로 부터 POST요청을 통해 자소서를 받고 

  Spredict.py 라는 우리 팀이 직접만든 분석 모듈을 이용하여 결과값을 컨텍스트에 넣어 페이지로 전송합니다.

  메인 기능인 라이트앱에서 사용한 저희가 만든 분석 모듈은 
  
  자소서를 전처리한 뒤 딥러닝 파트에서 만든 h5 모델을 이용해서 분석을 하고 라벨링된 점수를 리턴해줍니다.

* 전처리부분의 불용어처리는 db에 저장하여 사용했고 형태소분석기는 호환성을 위해서 hannanum을 이용했습니다.

* Trend News 는 트랜드 기사찾기 기능입니다.

  클라이언트에게 요구받은 검색 키워드를 받고 trend 앱의 views 파일이 키워드를  
  
  db에서 검색해 기사들을 모두 가져와 리스트로만들어 템플릿에 보냈습니다.

  템플릿 필터,  템플릿 반복문으로 서버에서 보낸 리스트를 읽어들여서
  
  가져온 모든 기사들을 빠뜨리지 않고 뿌려 줄수 있었습니다.

