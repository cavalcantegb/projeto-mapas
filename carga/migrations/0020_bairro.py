# Generated by Django 2.2.16 on 2020-09-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0019_auto_20200928_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('idh', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
            ],
        ),
    ]
