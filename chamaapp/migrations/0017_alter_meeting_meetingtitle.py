# Generated by Django 5.0.1 on 2024-01-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaapp', '0016_alter_meeting_meetingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingTitle',
            field=models.CharField(max_length=50, null=True),
        ),
    ]