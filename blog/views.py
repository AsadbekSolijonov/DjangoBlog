import json

from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category
from itertools import groupby
from django.utils.timezone import localtime


# Create your views here.
def index(request, tag=None):
    if not tag:
        blogs = Blog.objects.order_by("-created")
    else:
        blogs = Blog.objects.filter(category__name__icontains=tag).order_by("-created")

    group_year = {}
    for key, group in groupby(blogs, lambda post: localtime(post.created).year):
        group_year[key] = list(group)

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    group_month = {}
    for key, group in groupby(blogs, lambda post: localtime(post.created).month):
        group_month[month_names.get(key, 'Unknown')] = list(group)

    categories = Category.objects.all()

    context = {
        "grouped_blogs_month": group_month,
        "grouped_blogs_year": group_year,
        "categories": categories,
        "count": {"year": len(group_year), "month": len(group_month), "blog": blogs.count()}
    }

    return render(request, "blog/index.html", context=context)


def home(request):
    return render(request, 'home/home.html')
