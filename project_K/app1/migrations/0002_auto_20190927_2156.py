# Generated by Django 2.2.5 on 2019-09-27 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created',
        ),
    ]