# Generated by Django 3.0.1 on 2019-12-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_img', models.CharField(max_length=2083)),
                ('blog_author', models.CharField(max_length=200)),
            ],
        ),
    ]
