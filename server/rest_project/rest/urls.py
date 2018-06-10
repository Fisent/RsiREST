from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import new_method

urlpatterns = [
    path('new_method', new_method)
]