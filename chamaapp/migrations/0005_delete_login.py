# Generated by Django 5.0.1 on 2024-01-20 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamaapp', '0004_remove_login_id_login_profile_user_id_login_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
