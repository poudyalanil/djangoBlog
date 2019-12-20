from django.db import models


class BlogsPost(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_img = models.CharField(max_length=2083)
    blog_author = models.CharField(max_length=200)
