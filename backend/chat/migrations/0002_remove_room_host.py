# Generated by Django 4.1.5 on 2023-02-01 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
    ]
