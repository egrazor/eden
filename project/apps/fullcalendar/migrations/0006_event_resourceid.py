# Generated by Django 3.0.5 on 2020-04-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0005_remove_event_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resourceId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]