# Generated by Django 4.2.2 on 2023-10-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_room', '0007_user_is_verify_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubleroom',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
