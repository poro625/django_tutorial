from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index), # URL(index)  을 먼저 작성해주고 작성된 URL이 views.py안에 있는 index 로 이어질지를 뒤에 명시를 하게 해준다. 그리고 이어지기 위해서  views.py로가서 index라는 함수를 만들어야한다
    path('dinner/<str:name>/',views.dinner),# 주소자체를 변수처럼 이용해서 동적으로 주소를 만드는것을 칭한다 자주쓰이는것이 유저 개개인의 페이지(이런경우는 유저명이 주소로 들어가기때문에)
                                            # <str:name>으로 적고 name이라는 변수를 집어넣겠다 name은 뷰에서 받아올 수 있다.
    path('review/',views.review, name='review'), # name='review' url 뒤쪽에 이러한 형태로 적어주게되면 장고한테 장고 템플릿 랭귀지를 이용해서 name='review'을 명시하면 'review/' 이주소를 알아서 찾아서 보내준다
    path('create_review/',views.creative_review, name='creative_review'), # review.html에서 1번째줄 <form action="/create_review/" method="POST">부분에서 action="/create_review이리 선언했기 때문에 url을 잡아줘야한다 
]