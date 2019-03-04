from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .views import user_api

urlpatterns = [
    url('user_api/', user_api),
]