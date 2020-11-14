# Generated by Django 2.2.5 on 2019-10-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('purpose', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]