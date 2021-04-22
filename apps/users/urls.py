# -*- coding: utf-8 -*-
# @Time       :   2021-04-21 19:48
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
