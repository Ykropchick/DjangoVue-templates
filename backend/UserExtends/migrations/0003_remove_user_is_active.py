# Generated by Django 4.1.5 on 2023-01-24 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserExtends', '0002_remove_user_time_registrate_alter_user_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]