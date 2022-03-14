# Generated by Django 4.0.3 on 2022-03-13 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookMyRoomApp', '0007_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotels_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookMyRoomApp.hotels')),
            ],
        ),
    ]
