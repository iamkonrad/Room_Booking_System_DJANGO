# Generated by Django 4.2.3 on 2023-07-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0013_remove_conferenceroom_room_number_conferenceroom_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conferenceroom',
            name='id',
        ),
        migrations.AlterField(
            model_name='conferenceroom',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
