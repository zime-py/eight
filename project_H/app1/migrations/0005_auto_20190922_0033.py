# Generated by Django 2.2.5 on 2019-09-21 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='about',
        ),
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
        migrations.RemoveField(
            model_name='post',
            name='country',
        ),
    ]