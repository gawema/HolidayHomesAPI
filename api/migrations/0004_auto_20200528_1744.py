# Generated by Django 3.0.6 on 2020-05-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200528_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
