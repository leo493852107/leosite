#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-11-04"

'''

这个文件存放自定义的模板标签代码

'''

from django import template
from django.db.models.aggregates import Count
from blog.models import Blog, Category, Tag


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
    # 参考: http://zmrenwu.com/post/38/
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)

