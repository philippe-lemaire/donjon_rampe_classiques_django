# Generated by Django 4.1.3 on 2022-11-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="init",
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
