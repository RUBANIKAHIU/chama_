# Generated by Django 5.0.1 on 2024-01-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaapp', '0019_alter_meeting_meetingtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingDescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingTitle',
            field=models.CharField(max_length=50),
        ),
    ]
