# Generated by Django 2.2.16 on 2020-10-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0020_bairro'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='children_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
