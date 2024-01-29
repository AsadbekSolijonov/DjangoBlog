from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from itertools import groupby
from django.utils.timezone import localtime


# Create your views here.
def index(request):
    blogs = Blog.objects.order_by("-created")

    context = {}
    for key, group in groupby(blogs, lambda post: localtime(post.created).date()):
        context[key] = list(group)

    context = {
        "grouped_blogs": context
    }

    return render(request, "blog/index.html", context=context)


def hello(request):  # new
    return HttpResponse("<h1>Hello Asadbek</h1>")
