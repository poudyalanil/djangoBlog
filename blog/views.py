from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogsPost
import datetime


def index(request):

    month = datetime.datetime.now().strftime("%B")
    all_data = BlogsPost.objects.all()
   # latest_data = BlogsPost.objects.latest('date_added')
    # print(all_data)
    return render(request, "index.html", {"pg_title": 'Home', "home_is_active": 'active', "month": month, 'posts': all_data})


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
