import imp
from django.contrib import admin
from django.urls import path , include  # App을 추가함으로써 url관리에 있어서 혼선을 가지고 올 수 있기 때문에 include함수를 생성하고 활용해야한다
# from articles import views            # articles폴더에 들어가면 __init__.py라는게 보인다 그래서 파이썬이 articles폴더를 모듈로 인식하게 된다. include를 할시 articles내에 url.py를 생성해서 관리하기때문에 필요없어서 삭제해준다


urlpatterns = [


    path('admin/', admin.site.urls),            # URL(admin)을 먼저 작성해주고 작성된 URL이 어느함수(admin.site.urls) 로 이어질지를 뒤에 명시를 하게 해준다.    
    path('articles/',include('articles.urls')), #include함수를 생성하고 foods라는 앱을 만들었기 때문에 겹쳐지거나 이러한 경우에 혼선을 빚을 수 있다 따라서 이러한 경우를 예방하기 위해 인클루드를 사용하는 것이다 그리고 articles관련된 url듫을 articles앱안에 url.py를 만들어서 그곳에서 관리하도록 한다
                                                # url부분중에서 articles/ 뒤에 주소는 articles/(.url.py)에서 확인후에 붙여준다.
    #path('foods/',include('foods.urls')),

]
