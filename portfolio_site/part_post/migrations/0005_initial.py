# Generated by Django 4.2.2 on 2023-08-15 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('part_post', '0004_remove_newpost_user_delete_comment_delete_newpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_new_post', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('data_published', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('new_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_new_post', to='part_post.newpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
