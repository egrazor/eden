# Generated by Django 3.0.5 on 2020-04-29 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cources', '0005_auto_20200429_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_head', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='direction',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direction_department', to='cources.Department'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dean',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_dean', to=settings.AUTH_USER_MODEL),
        ),
    ]
