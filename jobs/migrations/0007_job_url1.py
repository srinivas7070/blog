# Generated by Django 2.0.7 on 2019-12-27 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_remove_job_url1'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url1',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
