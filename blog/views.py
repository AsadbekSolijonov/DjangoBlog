from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


# Create your views here.
def index(request):
    objects = Blog.objects.all()

    context = ""
    for obj in objects:
        context += F"<h1>{obj.title}</h1>"
        context += F"<h2>{obj.body}</h2>"

    return HttpResponse(f"{context}")


def hello(request):  # new
    return HttpResponse("<h1>Hello Asadbek</h1>")
