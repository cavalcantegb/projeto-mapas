# Generated by Django 2.2.15 on 2020-09-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0002_auto_20200902_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='registration_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='registration_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]