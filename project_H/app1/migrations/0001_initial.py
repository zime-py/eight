# Generated by Django 2.2.5 on 2019-09-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_group', models.CharField(blank=True, choices=[('PRE-SALES', 'PRE-SALES'), ('SALES', 'SALES'), ('SERVICE', 'SERVICE')], max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
