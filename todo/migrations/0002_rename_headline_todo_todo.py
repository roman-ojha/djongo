# Generated by Django 4.0.6 on 2022-07-18 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='headline',
            new_name='todo',
        ),
    ]