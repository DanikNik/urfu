# Generated by Django 2.1 on 2018-08-27 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_person_events'),
        ('event', '0003_auto_20180827_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='projects',
            field=models.ManyToManyField(through='event.Membership', to='event.Project'),
        ),
    ]
