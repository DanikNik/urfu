# Generated by Django 2.1 on 2018-08-23 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_person_events'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
    ]
