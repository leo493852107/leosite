#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-11-04"

'''

这个文件存放自定义的模板标签代码

'''

from django import template

from blog.models import Blog, Category


register = template.Library()


@register.simple_tag
def get_recent_blogs(num=5):
    """
    获取最新文章，默认取5篇
    参考: http://zmrenwu.com/post/12/
    """
    return Blog.objects.all()[:num]
    # return Blog.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def archives():
    return Blog.objects.dates("create_time", "month", order="DESC")


@register.simple_tag
def get_categories():
    return Category.objects.all()
