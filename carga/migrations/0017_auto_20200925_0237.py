# Generated by Django 2.2.16 on 2020-09-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0016_auto_20200921_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='google_plus',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
