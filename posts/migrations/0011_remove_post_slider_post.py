# Generated by Django 3.1.7 on 2021-04-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210405_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slider_post',
        ),
    ]
