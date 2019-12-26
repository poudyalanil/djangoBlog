from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogsPost
import datetime


def index(request):

    month = datetime.datetime.now().strftime("%B")
    all_data = list(BlogsPost.objects.all())

    # getting latest blogs from the list all_data
    latest_data = []
    for data in all_data[-1:]:
        latest_data.append(data)

    # getting some blogs for recommendation part
    related_post = []
    for data in all_data[0:3]:
        related_post.append(data)

    return render(request, "index.html", {"pg_title": 'Home',
                                          "home_is_active": 'active',
                                          "month": month,
                                          'head_posts': latest_data,
                                          'related_post': related_post, })


def about(request):
    is_active = "active"
    pg_title = "About Us"
    return render(request, "about.html", {"pg_title": pg_title,  "abt_is_active": is_active})


def contact(request):
    is_active = "active"
    pg_title = "Contact Us"
    return render(request, "contact.html", {"pg_title": pg_title,  "con_is_active": is_active})


def single(request):

    return render(request, "single.html", {"pg_title": 'title'})
