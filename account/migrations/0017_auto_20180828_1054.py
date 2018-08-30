# Generated by Django 2.1 on 2018-08-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20180828_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='fb_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='google_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='group_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='person',
            name='job_position',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='person',
            name='place_of_study',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='place_of_work',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='tg_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='vk_link',
            field=models.URLField(blank=True),
        ),
    ]
