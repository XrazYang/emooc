# -*- coding: utf-8 -*-
# @Time       :   2021-04-29 14:52
# @Author     :   XrazYang
# @File       :   forms.py
# @Project    :   emooc


from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


# 图片验证码
class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()
