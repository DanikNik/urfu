# Generated by Django 2.1 on 2018-08-23 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20180823_2329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
    ]
