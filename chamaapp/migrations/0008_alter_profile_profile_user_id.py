# Generated by Django 5.0.1 on 2024-01-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaapp', '0007_members_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
