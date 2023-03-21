from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):# 첫번째 파라미터는 항상 reqeust
    posts = Post.objects.all().order_by("created_at")

    return render(
        request, #고정 암기할래그
        'blog/index.html',
        {
            'posts':posts,
        }
    )
def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post
        }
    )