# -*- coding: utf-8 -*-
# @Time       :   2021-05-03 12:21
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from apps.organization.views import OrgView

urlpatterns = [
    path('org_list/', OrgView.as_view(), name='org_list'),
]
