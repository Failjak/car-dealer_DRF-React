# Generated by Django 4.0.4 on 2022-04-24 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_offer_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cars',
        ),
    ]