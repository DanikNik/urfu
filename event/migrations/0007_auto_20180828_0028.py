# Generated by Django 2.1 on 2018-08-28 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_person_projects'),
        ('event', '0006_auto_20180828_0017'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Membership',
            new_name='ProjectMembership',
        ),
    ]
