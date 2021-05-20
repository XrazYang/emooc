"""emooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from django.views.static import serve

import xadmin

from apps.users import urls as users_urls
from emooc.settings import MEDIA_ROOT

urlpatterns = [
    path('', include(users_urls)),
    # path('', include(org_urls)),
    url(r'^org/', include(('apps.organization.urls', 'organization'), namespace='org')),
    url(r'^op/', include(('apps.operation.urls', 'operation'), namespace='op')),
    url(r'^course/', include(('apps.courses.urls', 'courses'), namespace='course')),

    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('captcha/', include('captcha.urls')),
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),  # 配置上传文件访问
]
