# Generated by Django 5.1.5 on 2025-02-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_room_current_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='previous_song',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='current_song',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
