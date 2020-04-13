from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import DetailObjectMixin

def posts_list(request):
    posts = Post.objects.all()
    return render(request, "blog/posts_list.html", context={"posts": posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tags_list.html", context={"tags": tags})


class PostDetail(DetailObjectMixin, View):
    model = Post
    template = "blog/post_detail.html"


class TagDetail(DetailObjectMixin, View):
    model = Tag
    template = "blog/tag_detail.html"
