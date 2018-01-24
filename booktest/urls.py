#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'(?P<p1>\d+)/(?P<p2>\d+)/(?P<p3>\d+)/$',views.detail),#(\d+)小括号的意思代表取一个值
    url(r'^$', views.index),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
    url(r'^postTest1/$',views.postTets1),
    url(r'^postTest2/$', views.postTets2),
]