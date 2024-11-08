# Generated by Django 4.2.7 on 2023-11-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("refxpert", "0014_houseapplication_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenantform",
            name="employer",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="tenantform",
            name="employer_address",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="tenantform",
            name="employer_phone",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="tenantform",
            name="job_title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]