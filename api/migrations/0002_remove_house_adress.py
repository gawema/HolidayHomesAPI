# Generated by Django 3.0.6 on 2020-05-05 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='adress',
        ),
    ]
