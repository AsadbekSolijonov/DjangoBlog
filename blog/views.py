from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


# Create your views here.
def index(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }

    return render(request, "blog/index.html", context=context)


def hello(request):  # new
    return HttpResponse("<h1>Hello Asadbek</h1>")
