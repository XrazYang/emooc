# -*- coding: utf-8 -*-
# @Time       :   2021-05-19 11:48
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc


from django.urls import path
from django.conf.urls import url
from apps.operation.views import AddFavView

urlpatterns = [
    # path('org_list/', OrgView.as_view(), name='org_list'),
    url(r'^fav/$', AddFavView.as_view(), name='fav'),
]
