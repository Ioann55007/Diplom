# Generated by Django 4.2.2 on 2023-10-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_profile', '0002_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
