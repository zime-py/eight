# Generated by Django 3.1.1 on 2020-09-01 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0004_auto_20200901_2134'),
        ('app1', '0002_customuser_roll'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='lol',
        ),
    ]
