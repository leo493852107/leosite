from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Blog

# Create your views here.


# def index(request):
#     return render(request, "blog/index.html", {
#         ""
#     })

class BlogListView(View):
    """博客列表页"""
    def get(self, request):
        all_blogs = Blog.objects.all().order_by('create_time')

        return render(request, 'blog/index.html', {
            'all_blogs': all_blogs,
        })


class BlogDetailView(View):
    """博客详情页"""
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=int(blog_id))

        # 增加博客点击数
        blog.read_num += 1
        blog.save()

        return render(request, "blog/blog_detail.html", {
            "blog": blog,

        })


