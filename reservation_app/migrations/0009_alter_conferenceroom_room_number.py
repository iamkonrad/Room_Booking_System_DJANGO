# Generated by Django 4.2.3 on 2023-07-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0008_conferenceroom_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferenceroom',
            name='room_number',
            field=models.CharField(default='101', max_length=255),
        ),
    ]