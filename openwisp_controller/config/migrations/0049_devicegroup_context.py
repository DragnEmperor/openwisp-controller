# Generated by Django 3.2.19 on 2023-06-27 14:45

import collections

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("config", "0048_wifi_radio_band_migration"),
    ]

    operations = [
        migrations.AddField(
            model_name="devicegroup",
            name="context",
            field=jsonfield.fields.JSONField(
                blank=True,
                default=dict,
                dump_kwargs={"ensure_ascii": False, "indent": 4},
                help_text=(
                    "This field can be used to add meta data for the group"
                    ' or to add "Configuration Variables" to the devices.'
                ),
                load_kwargs={"object_pairs_hook": collections.OrderedDict},
                verbose_name="Configuration Variables",
            ),
        ),
    ]
