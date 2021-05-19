# -*- coding: utf-8 -*-
# @Time       :   2021-05-19 11:54
# @Author     :   XrazYang
# @File       :   forms.py
# @Project    :   emooc

from django import forms
from apps.operation.models import UserFavorite


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]
