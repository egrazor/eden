# Generated by Django 3.0.5 on 2020-04-29 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cources', '0004_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='degree',
            field=models.CharField(blank=True, choices=[('bachelor', 'Бакалавриат'), ('master', 'Магистратура')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='department_head', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='direction',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='direction_department', to='cources.Department'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dean',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='faculty_dean', to=settings.AUTH_USER_MODEL),
        ),
    ]
