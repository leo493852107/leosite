from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags

import markdown

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="标签")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Blog(models.Model):
    """博客"""
    title = models.CharField(verbose_name="标题", max_length=100)
    # abstract = models.CharField(verbose_name="摘要", max_length=200, blank=True)
    content = models.TextField(verbose_name="内容")
    read_num = models.PositiveIntegerField(verbose_name="浏览数", default=0)
    comment_num = models.IntegerField(verbose_name="评论数", default=0)
    create_time = models.DateTimeField(verbose_name="创建日期")
    update_time = models.DateTimeField(verbose_name="修改日期")

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True, verbose_name="摘要")
    category = models.ForeignKey(Category, verbose_name="分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name
        # 在模型中指定排序  参考:http://zmrenwu.com/post/16/
        ordering = ["-create_time"]

    def increase_views(self):
        """
        阅读数 + 1
        相当于封装了方法, 供 blog/views.py 中调用
        """
        self.read_num += 1
        # 注意这里使用了 update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率。
        self.save(update_fields=['read_num'])

    def get_absolute_url(self):
        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
        return reverse("blog:detail", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.content))[:54] + "..."

        # 调用父类的 save 方法将数据保存到数据库中
        super(Blog, self).save(*args, **kwargs)
