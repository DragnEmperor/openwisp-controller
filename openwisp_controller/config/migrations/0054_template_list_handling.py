# Generated by Django 4.2.7 on 2023-11-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0053_vpnclient_secret"),
    ]

    operations = [
        migrations.AddField(
            model_name="template",
            name="list_handling",
            field=models.CharField(
                choices=[
                    ("insert_at_beginning", "Insert items at the beginning"),
                    ("append_at_end", "Append items at the end"),
                    ("override", "Override all items"),
                ],
                db_index=True,
                default="append_at_end",
                help_text="list handling, determines how list items in this "
                "template are handled if the same list exists in a previously"
                " applied template",
                max_length=20,
                verbose_name="list handling",
            ),
        ),
    ]
