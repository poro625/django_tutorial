#실질적으로 API 로직들을 작성하는곳

from ast import If
from cmd import IDENTCHARS
from multiprocessing import context
import random
from django.shortcuts import render


def index(request):        
    return render(request, 'index.html')   


    # django_tutorial/urls.py/ 안에있는 9번째줄 path('index/', views.index) index랑 일치해야한다. URL과 veiw를 설정하였기 때문에 veiw에서 index.html를 설정하여 연결을 지어줘야한다.
    # index.html를 만들기 위해 templates폴더를 만들고 안에 index.html를만들자
    # *request는 무조건 첫번째 인자로 받아야한다 *
    # return으로 render를 해서 request인자와 index.html를 다룬다. request는 render에 첫번째 인자로 불러줘야한다

def dinner(request, name):

    menus = [{'name':'족발','price' : 30000},{'name':'햄버거','price':20000},{'name':'치킨','price':5000},{'name':'초밥','price':10000}]
    pick = random.choice(menus)

    context = {
        'pick' : pick,  # 'pick' : pick중에서 'pick'값은 키값으로 변수로 생각하면 편하다 두번째 ''가없는 pick값이 메뉴중에서 랜덤으로 선택되서 담기는 것이다.
        'name' : name,  # URL에서 선언된<str:name> 이부분에서 변수를 만들어서 연결시켜준다.
        'menus' : menus

    }

    return render(request, 'dinner.html' , context)


    # 19번째줄 random.choice(menus)는 메뉴안에 있는것중에서 랜덤으로 고른다는 뜻이다 랜덤으로 골라진것들이 pick이라는 변수로 들어가진다
    # 22번째줄을 보면 veiws.py에서 dinner.html로 데이터를 넘겨주기 위해서 context라는 변수를 사용할 것이다 이런한 context라는 변수를 27번째 줄에 실어준다 html 부분에서는 context안에 있는 내가 지칭한 변수 키값을 쓸것이다.

def review(request):

    return render(request, 'review.html')   

def creative_review(request):

    content = request.POST.get('content') # review.html에서 request를 통해서 받은것중 POST일때 데이터안에서 content라는걸 받아온다 그리고 get으로 조율할 수 있게된다 ('content')는  review.html에서 name="content"
    print(request.POST)
    context = {

        'content' : content,

    }

    return render(request, 'review_result.html' , context)