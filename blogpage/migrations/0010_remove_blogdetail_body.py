# Generated by Django 5.0.7 on 2024-08-07 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpage', '0009_remove_blogdetail_blog_author_blogpagetag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetail',
            name='body',
        ),
    ]
