#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-11-04"



from django.conf.urls import url

from comments.views import blog_comment


# 规定命名空间
app_name = "comments"

urlpatterns = [
    # 评论页
    url(r'^comment/post/(?P<blog_pk>\d+)/$', blog_comment, name="blog_comment"),


]

