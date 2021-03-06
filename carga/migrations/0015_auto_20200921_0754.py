# Generated by Django 2.2.16 on 2020-09-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0014_agentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('subscription_number', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('project_name', models.TextField()),
                ('user_name', models.TextField()),
                ('location', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('points', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('location_type', models.CharField(blank=True, choices=[('municipio', 'Municipio'), ('bairro', 'Bairro')], max_length=60, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='agentdata',
            name='geoMunicipio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
