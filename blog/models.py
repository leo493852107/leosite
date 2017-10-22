from django.db import models

# Create your models here.


class Blog(models.Model):
    """博客"""
    title = models.CharField(verbose_name="标题", max_length=100)
    abstract = models.CharField(verbose_name="摘要", max_length=200)
    content = models.TextField(verbose_name="内容")
    read_num = models.IntegerField(verbose_name="浏览数", default=0)
    comment_num = models.IntegerField(verbose_name="评论数", default=0)
    create_time = models.DateField(verbose_name="创建日期")
    update_time = models.DateField(verbose_name="修改日期")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

