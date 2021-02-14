# Generated by Django 3.1.3 on 2021-01-23 21:19

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addrespoint",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("31f60760-c7bb-4c5c-940d-8866733b2d73"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="addrespoint",
            name="street",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="archive_manager.street",
            ),
        ),
        migrations.AlterField(
            model_name="buildings",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("d76dad0c-a2dd-466f-9b74-c1b86838027e"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
