# Generated by Django 2.1 on 2018-08-28 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20180828_1444'),
        ('event', '0008_eventmembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(through='event.EventMembership', to='account.Person'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_required',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_events', to='account.Person'),
        ),
    ]