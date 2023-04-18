from django.contrib import admin
from django.urls import path
from crud1 import views
urlpatterns = [
    path('', views.crud1, name='crud1'),
    path('crud', views.crud, name='crud'),
]