"""my_dj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.urls import path

from django.conf.urls import url
from django.contrib import admin
from blogs import views
from blogs.views import *
from django.conf.urls import *
from blogs.models import *


urlpatterns = [

    url(r'^admin/',admin.site.urls),
    # url(r'^$',views.home),
    # path('admin/', admin.site.urls),
    # path(r'hello/',hello),
    # # path(r'hello_0/',hello_0),
    # # # path(r'hello_1/',hello_1),
    # # path(r'hello_2/',hello_2),
    # path(r'home/',home),
    # # path(r'hello_3/',hello_3),
    # path(r'base/',base),
    # path(r'test/',test),
    # path(r'test2/',test2),
    # path(r'userinfo/',userinfo),
    # path(r'add/',add),
    # path(r'select/',select),
    url(r'^home/$',home,name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    # url(r'test3/$',views.test),
    # url(r'^home/$',home,name='home'),
    # re_path(r'home/^(?P<id>\d+)/$', detail, name='detail'),
    #url(r'^(?P<id>\d+)/$',detail,name='detail'),
]
