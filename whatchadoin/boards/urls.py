from django.conf.urls import url, include
from .views import boards_home, board, api_boards

from boards.api import views

app_name = 'boards'


urlpatterns = [

    url(r'^$', boards_home, name="boards_home"),

    url(r'^(?P<board_id>[0-9]+)/$', board, name='board'),
    url(r'^api/$', views.BoardViewSet.as_view()),
    url(r'^api-boards/$', api_boards, name='api_boards'),


]
