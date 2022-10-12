#앱에 정보가 담겨있고 딱히 수정할 필요는 없다

from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
