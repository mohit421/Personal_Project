# Generated by Django 5.1.5 on 2025-02-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_room_previous_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='current_volume',
            field=models.IntegerField(default=50),
        ),
    ]
