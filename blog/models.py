from django.db import models
from django.urls import reverse

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
    read_num = models.IntegerField(verbose_name="浏览数", default=0)
    comment_num = models.IntegerField(verbose_name="评论数", default=0)
    create_time = models.DateTimeField(verbose_name="创建日期")
    update_time = models.DateTimeField(verbose_name="修改日期")

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def increase_views(self):
        """
        阅读数 + 1
        相当于封装了方法, 供 blog/views.py 中调用
        """
        self.read_num += 1
        self.save()

    def get_absolute_url(self):
        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
        return reverse("blog:detail", kwargs={'pk': self.pk})
