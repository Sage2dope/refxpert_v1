# Generated by Django 4.2.7 on 2024-11-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refxpert', '0020_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
