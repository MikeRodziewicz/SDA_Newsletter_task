# Generated by Django 3.1.3 on 2020-11-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20201126_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address_one',
            field=models.CharField(default=None, max_length=280),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_two',
            field=models.CharField(default=None, max_length=280),
        ),
    ]
