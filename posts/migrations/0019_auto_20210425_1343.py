# Generated by Django 3.1.7 on 2021-04-25 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0018_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='publishing_date')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='image')),
                ('slug', models.SlugField(default='slug', editable=False, verbose_name='slug')),
                ('slider_post', models.BooleanField(default=False, verbose_name='slider_post')),
                ('hit', models.PositiveIntegerField(default=0, verbose_name='hit')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='archives', to='posts.category')),
                ('main_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, related_name='archives', to='posts.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
