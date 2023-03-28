from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.
# def index(request):# 첫번째 파라미터는 항상 reqeust
#     posts = Post.objects.all().order_by("created_at")
#
#     return render(
#         request, #고정 암기할래그
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )
class PostList(ListView): #목록 보기화면 완성
    model = Post


# def single_post_page(request, post_num):
#     post = Post.objects.get(pk=post_num)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post':post
#         }
#     )

class PostDetail(DetailView):
    model = Post
