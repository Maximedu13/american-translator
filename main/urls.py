from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include, url

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]
