from django.shortcuts import render
import sqlite3
import pandas as pd
import numpy as np

# Create your views here.


def trendview(request):
    if request.method == 'POST':
        try:
            search_db = sqlite3.connect('db.sqlite3')
            search_word = request.POST['searchword']
            search_pd = pd.read_sql_query(
                f"select title,content from news_complete WHERE content LIKE '%{search_word}%' ", search_db)
            temp = search_pd.to_numpy()
            temp2 = temp.tolist()
            # {'title': temp2[0][0], 'content': temp2[0][1]}
            context = {'file': temp2}
            # for idx, i in enumerate(temp2):
            #     mkdic = {'title': i[0], 'content': i[1]}
            #     context[idx] = mkdic

            return render(request, 'trend/searchrst.html', context)
        except IndexError:
            return render(request, 'trend/trend.html')

    else:
        return render(request, 'trend/trend.html')
