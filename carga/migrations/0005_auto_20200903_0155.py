# Generated by Django 2.2.15 on 2020-09-03 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0004_auto_20200902_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='areas',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_long',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_short',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='opportunity_tab_name',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='parent_entity',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_facebook',
            field=models.URLField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_goal',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_google_plus',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_instagram',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_twitter',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_website',
            field=models.URLField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='published_by',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stamps',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='target_audience',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
