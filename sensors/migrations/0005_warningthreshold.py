# Generated by Django 3.1.12 on 2021-08-25 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sensors", "0004_auto_20210825_2151"),
    ]

    operations = [
        migrations.CreateModel(
            name="WarningThreshold",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "max_temperature",
                    models.FloatField(
                        blank=True, help_text="Maximum temperature threshold", null=True
                    ),
                ),
                (
                    "min_temperature",
                    models.FloatField(
                        blank=True, help_text="Minimum temperature threshold", null=True
                    ),
                ),
                (
                    "max_humidity",
                    models.FloatField(
                        blank=True, help_text="Maximum humidity threshold", null=True
                    ),
                ),
                (
                    "min_humidity",
                    models.FloatField(
                        blank=True, help_text="Minimum humidity threshold", null=True
                    ),
                ),
                (
                    "max_pressure",
                    models.FloatField(
                        blank=True, help_text="Maximum pressure threshold", null=True
                    ),
                ),
                (
                    "min_pressure",
                    models.FloatField(
                        blank=True, help_text="Minimum pressure threshold", null=True
                    ),
                ),
                (
                    "max_battery",
                    models.FloatField(
                        blank=True,
                        help_text="Maximum battery voltage threshold",
                        null=True,
                    ),
                ),
                (
                    "min_battery",
                    models.FloatField(
                        blank=True,
                        help_text="Minimum battery voltage threshold",
                        null=True,
                    ),
                ),
                (
                    "sensor",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="warning_thresholds",
                        to="sensors.sensor",
                    ),
                ),
            ],
        ),
    ]
