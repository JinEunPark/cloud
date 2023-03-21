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