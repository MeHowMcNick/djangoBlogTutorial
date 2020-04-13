from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_list(request):
    posts = Post.objects.all()
    return render(request, "blog/posts_list.html", context={"posts": posts})


def post_detail(request, slug):
    try:
        post = Post.objects.get(slug__iexact=slug)
        return render(request, "blog/post_detail.html", context={"post": post})
    except:
        return render(request, "blog/post_detail.html", context={"post": "This post does not exist."})
