from django.db import models


# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name="昵称")
    email = models.EmailField(max_length=255, verbose_name="邮件")
    url = models.URLField(blank=True, verbose_name="链接")
    text = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    blog = models.ForeignKey("blog.Blog")

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

