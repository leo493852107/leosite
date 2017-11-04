#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-10-22"


from django.conf.urls import url

from blog.views import BlogListView, BlogDetailView, ArchivesView, CategoryView


app_name = "blog"

urlpatterns = [
    # 博客列表页
    url(r'^$', BlogListView.as_view(), name="list"),

    # 博客详情页
    url(r'^detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="detail"),

    # 博客归档页
    url(r'^archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$', ArchivesView.as_view(), name="archives"),

    # 博客分类页
    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view(), name="category"),

]

