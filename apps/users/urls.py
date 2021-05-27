# -*- coding: utf-8 -*-
# @Time       :   2021-04-21 19:48
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from django.conf.urls import url
from .views import LoginView, RegisterView, LogoutView, SendSmsView, DynamicLoginView, UserInfoView, UploadImageView, \
    ChangePwdView, ChangeMobileView, MyCourseView, MyFavCourseView, MyFavTeacherView, MyFavOrgView, MyMessageView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dynamic_login/', DynamicLoginView.as_view(), name='dynamic_login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', csrf_exempt(RegisterView.as_view()), name='register'),
    path('send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),

    url(r'^info/$', UserInfoView.as_view(), name='info'),
    url(r'^mycourses/$', MyCourseView.as_view(), name='mycourses'),
    url(r'^mymessages/$', MyMessageView.as_view(), name='mymessages'),
    url(r'^favcourses/$', MyFavCourseView.as_view(), name='favcourses'),
    url(r'^favorgs/$', MyFavOrgView.as_view(), name='favorgs'),
    url(r'^favteachers/$', MyFavTeacherView.as_view(), name='favteachers'),

    url(r'^image/upload/$', UploadImageView.as_view(), name='image'),
    url(r'^update/pwd/$', ChangePwdView.as_view(), name='pwd'),
    url(r'^update/mobile/$', ChangeMobileView.as_view(), name='mobile'),
]
