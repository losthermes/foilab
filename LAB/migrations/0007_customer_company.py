# Generated by Django 2.2.2 on 2019-08-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LAB', '0006_auto_20190727_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
