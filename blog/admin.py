from django.contrib import admin
from .models import BlogsPost
# importing class name(BlogsPost) from models of app blog

admin.site.register(BlogsPost)
