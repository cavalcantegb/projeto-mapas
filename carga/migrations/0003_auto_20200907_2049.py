# Generated by Django 2.2.15 on 2020-09-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0002_auto_20200907_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_goal',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]