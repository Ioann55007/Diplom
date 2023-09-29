# Generated by Django 4.2.2 on 2023-09-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('part_room', '0004_remove_room_adults_remove_room_arrival_date_and_more'),
        ('the_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text_review', models.TextField()),
                ('name_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_author', to='the_profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BookingHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateTimeField()),
                ('date_of_departure', models.DateTimeField()),
                ('adults', models.PositiveIntegerField()),
                ('childs', models.PositiveIntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('room_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_room.room')),
                ('user_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_profile.profile')),
            ],
        ),
    ]