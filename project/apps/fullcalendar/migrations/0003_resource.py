# Generated by Django 3.0.5 on 2020-04-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0002_auto_20200421_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('eventBackgroundColor', models.CharField(default='#3788d8', max_length=50)),
                ('eventTextColor', models.CharField(default='#fff', max_length=50)),
                ('eventClassNames', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
