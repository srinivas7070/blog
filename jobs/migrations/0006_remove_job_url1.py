# Generated by Django 2.0.7 on 2019-12-27 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_url1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='url1',
        ),
    ]
