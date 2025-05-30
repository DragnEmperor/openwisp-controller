# Generated by Django 3.2.15 on 2022-09-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("config", "0044_config_error_reason"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vpn",
            name="webhook_endpoint",
            field=models.URLField(
                blank=True,
                help_text=(
                    "Webhook to trigger for updating server configuration"
                    " (e.g. https://openwisp2.mydomain.com:8081/trigger-update)"
                ),
                null=True,
                verbose_name="Webhook Endpoint",
            ),
        ),
    ]
