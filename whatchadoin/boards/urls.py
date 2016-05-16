from django.conf.urls import url
from .views import boards_home, board
from django.contrib.auth import views as auth_views

app_name = 'boards'

urlpatterns = [

    url(r'^$', boards_home, name="boards_home"),
    url(r'^(?P<board_id>[0-9]+)/$', board, name='board')

]
