"""whatchadoin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import login, profile, register
from boards.api import views

# router for Admin to view all users
from rest_framework import routers

# setting up router for admin view
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Auth login
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^login/', login),
    url(r'^profile/', profile),
    url(r'^register/', register),
    url(r'^boards/', include('boards.urls')),

    # Takes in the users from the router
    url(r'^', include(router.urls)),

    url(r'^$', include('home.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

