# Generated by Django 2.1.5 on 2019-02-11 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190211_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='email_1',
        ),
    ]
