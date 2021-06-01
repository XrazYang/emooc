from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')

    class Meta:
        abstract = True  # 不会生成表


'''
    通过继承AbstractUser，扩展auth_user表
'''


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')  # 可以为空，或者defaul 设置默认值
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=6)
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='联系方式')
    head_image = models.ImageField(upload_to='head/%Y/%m', verbose_name='用户头像', default="head/default.jpg")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        return self.username

    def unread_nums(self):
        return self.usermessage_set.filter(has_read=False).count()
