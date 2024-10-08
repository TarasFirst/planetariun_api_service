# Generated by Django 5.1 on 2024-09-04 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AstronomyShow",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("duration", models.IntegerField()),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="PlanetariumDome",
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
                ("name", models.CharField(max_length=255)),
                ("rows", models.IntegerField()),
                ("seats_in_row", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ShowTheme",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ShowSession",
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
                ("show_time", models.DateTimeField()),
                (
                    "astronomy_show",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="show_sessions",
                        to="planetarium_service.astronomyshow",
                    ),
                ),
                (
                    "planetarium_dome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="planetarium_service.planetariumdome",
                    ),
                ),
            ],
            options={
                "ordering": ["-show_time"],
            },
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="show_themes",
            field=models.ManyToManyField(
                blank=True,
                related_name="astronomy_shows",
                to="planetarium_service.showtheme",
            ),
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("row", models.IntegerField()),
                ("seat", models.IntegerField()),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="planetarium_service.reservation",
                    ),
                ),
                (
                    "show_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="planetarium_service.showsession",
                    ),
                ),
            ],
            options={
                "ordering": ["row", "seat"],
                "unique_together": {("show_session", "row", "seat")},
            },
        ),
    ]
