from django.contrib import admin

from blog import models


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "abstract", "content", "read_num",
                    "comment_num", "create_time", "update_time")


admin.site.register(models.Blog, BlogAdmin)


