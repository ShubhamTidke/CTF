# Generated by Django 2.1.5 on 2019-02-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_1', models.CharField(max_length=100)),
                ('email_1', models.EmailField(max_length=100)),
            ],
        ),
    ]
