from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    is_active = "active"
    pg_title = "Home"
    month = datetime.datetime.now().strftime("%B")

    return render(request, "index.html", {"pg_title": pg_title, "home_is_active": is_active, "month": month})


def about(request):
    is_active = "active"
    pg_title = "About Us"
    return render(request, "about.html", {"pg_title": pg_title,  "abt_is_active": is_active})


def contact(request):
    is_active = "active"
    pg_title = "Contact Us"
    return render(request, "contact.html", {"pg_title": pg_title,  "con_is_active": is_active})
