# Generated by Django 3.1.1 on 2020-09-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='roll',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
