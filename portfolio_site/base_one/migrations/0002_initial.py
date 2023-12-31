# Generated by Django 4.2.2 on 2023-10-03 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_one', '0001_initial'),
        ('the_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewhotel',
            name='name_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_author', to='the_profile.profile'),
        ),
        migrations.AddField(
            model_name='price',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_price', to='base_one.bookinghotel'),
        ),
        migrations.AddField(
            model_name='bookinghotel',
            name='user_booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_profile.profile'),
        ),
    ]
