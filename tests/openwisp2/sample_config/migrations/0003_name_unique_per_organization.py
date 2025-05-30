# Generated by Django 3.1.6 on 2021-02-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample_config", "0002_default_groups_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="template",
            name="name",
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="vpn",
            name="name",
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name="vpn", unique_together={("organization", "name")}
        ),
    ]
