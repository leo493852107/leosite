#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-10-22"


from django.conf.urls import url

from blog.views import BlogListView, BlogDetailView


urlpatterns = [
    # 博客列表页
    url(r'^list/$', BlogListView.as_view(), name="blog_list"),

    # 博客详情页
    url(r'^detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="blog_detail"),


]

