from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]