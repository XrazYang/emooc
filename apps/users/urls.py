# -*- coding: utf-8 -*-
# @Time       :   2021-04-21 19:48
# @Author     :   XrazYang
# @File       :   urls.py
# @Project    :   emooc

from django.urls import path
from .views import LoginView, RegisterView, LogoutView, SendSmsView, DynamicLoginView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dynamic_login/', DynamicLoginView.as_view(), name='dynamic_login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', csrf_exempt(RegisterView.as_view()), name='register'),
    path('send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),
]
