# Generated by Django 5.0.1 on 2024-01-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaapp', '0014_rename_description_meeting_meetingdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingDescription',
            field=models.TextField(blank=True, null=True),
        ),
    ]