# Generated by Django 2.2.5 on 2019-10-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
    ]