# -*- coding: utf-8 -*-
# @Time       :   2021-05-03 12:21
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from django.conf.urls import url
from apps.organization.views import OrgView, AddAskView, OrgHomeView, OrgTeacherView, OrgCourseView, OrgDescView, \
    TeacherListView

urlpatterns = [
    # path('org_list/', OrgView.as_view(), name='org_list'),
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddAskView.as_view(), name='add_ask'),
    url(r'^(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name='org_teacher'),
    url(r'^(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name='org_desc'),

    url(r'^teacher_list/$', TeacherListView.as_view(), name='teacher_list'),
    # path('<int:org_id>/', OrgHomeView.as_view(), name='org_home'),
]
