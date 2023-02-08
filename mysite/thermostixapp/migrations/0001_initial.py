# Generated by Django 4.1.6 on 2023-02-08 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Thermometer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("assignedUsers", models.ManyToManyField(to="thermostixapp.user")),
            ],
        ),
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("temperature", models.FloatField()),
                ("time", models.DateTimeField()),
                ("thermometer", models.ManyToManyField(to="thermostixapp.thermometer")),
            ],
        ),
    ]
