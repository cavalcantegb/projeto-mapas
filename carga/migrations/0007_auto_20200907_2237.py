# Generated by Django 2.2.15 on 2020-09-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0006_auto_20200907_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='tags',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
