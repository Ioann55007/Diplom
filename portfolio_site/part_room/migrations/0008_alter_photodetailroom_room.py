# Generated by Django 4.2.2 on 2023-08-21 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part_room', '0007_photodetailroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photodetailroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_room', to='part_room.room', verbose_name='Номер в гостинице'),
        ),
    ]
