# Generated by Django 3.1.7 on 2021-03-04 23:56

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive_manager", "0002_auto_20210304_2356"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adrespoint",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("b9a40507-945b-4bc4-ae84-adf2a38cfbc5"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="buildings",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("faac8df2-3e91-483d-858f-04f232db16f7"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
