# -*- coding: utf-8 -*-
# @Time       :   2021-05-03 12:21
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from django.conf.urls import url
from apps.organization.views import OrgView, AddAskView

urlpatterns = [
    # path('org_list/', OrgView.as_view(), name='org_list'),
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddAskView.as_view(), name='add_ask')
]
