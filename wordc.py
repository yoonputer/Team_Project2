import matplotlib.pyplot as plt
from wordcloud import WordCloud


def mkwdcrd(story, email):
    font_path = 'CREMA_MYUNGJO2B.ttf'  # 폰트설정

    wordcloud = WordCloud(
        max_words=200,  # 최대 수용 단어 갯수
        background_color='white',  # 배경색상
        font_path=font_path,
        width=800,  # 넓이
        height=800,  # 길이
        collocations=False,
    )

    # 대체하고 싶은 단어 입력
    text = story
    email1 = email
    wordcloud = wordcloud.generate(text)

    fig = plt.figure(figsize=(6, 6))  # 워드클라우드 사이즈 설정 6,6이 숫자덜 수정 가능
    plt.imshow(wordcloud)
    plt.axis("off")
    fig.savefig(f'static/write/{email1}.png')
