from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blog

# Create your views here.


class BlogListView(ListView):
    """
    博客列表页
    参考: https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
    """
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"
    paginate_by = 2
    queryset = Blog.objects.all().order_by("-create_time")


class BlogDetailView(DetailView):
    """
    博客详情页
    参考: http://zmrenwu.com/post/33/
    """

    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"

    def get(self, request, *args, **kwargs):
        response = super(BlogDetailView, self).get(request, *args, **kwargs)
        # 将文章阅读量 +1
        self.object.increase_views()
        # self.object.read_num += 1
        # self.object.save()
        return response

    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailView, self).get_context_data(**kwargs)
    #     return context


# class BlogListView(View):
#     """博客列表页"""
    # def get(self, request):
    #     all_blogs = Blog.objects.all().order_by('-create_time')
    #     limit = 2   # 每页显示的记录数
    #     paginator = Paginator(all_blogs, limit)     # 实例化一个分页对象
    #     page = request.GET.get('page')  # 获取页码
    #     try:
    #         blogs = paginator.page(page)    # 获取某页对应的记录
    #     except PageNotAnInteger:    # 如果页码不是个整数
    #         blogs = paginator.page(1)   # 取第一页的记录
    #     except EmptyPage:   # 如果页码太大，没有相应的记录
    #         blogs = paginator.page(paginator.num_pages)     # 取最后一页的记录
    #
    #     return render(request, 'blog/blog_list.html', {
    #         'blogs': blogs,
    #     })


# class BlogDetailView(View):
#     """
#     博客详情页
#     """
#     def get(self, request, blog_id):
#         blog = Blog.objects.get(id=int(blog_id))
#
#         # 增加博客点击数
#         blog.read_num += 1
#         blog.save()
#
#         return render(request, "blog/blog_detail.html", {
#             "blog": blog,
#
#         })

