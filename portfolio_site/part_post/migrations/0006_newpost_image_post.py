# Generated by Django 4.2.2 on 2023-09-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_post', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='image_post',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]