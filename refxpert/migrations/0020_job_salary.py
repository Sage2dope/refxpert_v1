# Generated by Django 4.2.7 on 2024-01-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("refxpert", "0019_remove_job_is_open_job_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="salary",
            field=models.CharField(blank=True, null=True),
        ),
    ]
