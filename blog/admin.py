from django.contrib import admin

from blog import models


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt", "read_num",
                    "comment_num", "create_time", "update_time")


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)

