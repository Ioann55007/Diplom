# Generated by Django 4.2.2 on 2023-08-15 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpost',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='NewPost',
        ),
    ]