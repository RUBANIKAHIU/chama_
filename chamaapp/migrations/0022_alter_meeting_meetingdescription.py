# Generated by Django 5.0.1 on 2024-01-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaapp', '0021_alter_meeting_meetingdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingDescription',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
