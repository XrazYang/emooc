# -*- coding: utf-8 -*-
# @Time       :   2021-05-20 14:40
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from django.conf.urls import url
from apps.courses.views import CourseListView, CourseDetailView, CourseLessonView

urlpatterns = [
    # path('org_list/', OrgView.as_view(), name='org_list'),
    url(r'^list/$', CourseListView.as_view(), name='list'),
    url(r'^(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name='lesson'),
]
