# Generated by Django 5.1 on 2024-09-01 14:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("planetarium_service", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="showsession",
            name="astronomyshow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="planetarium_service.astronomyshow",
            ),
        ),
        migrations.AddField(
            model_name="showsession",
            name="planetarium_dome",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="planetarium_service.planetariumdome",
            ),
        ),
        migrations.AddField(
            model_name="showtheme",
            name="astronomyshow",
            field=models.ManyToManyField(
                blank=True,
                related_name="astronomyshows",
                to="planetarium_service.astronomyshow",
            ),
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="showtheme",
            field=models.ManyToManyField(
                blank=True,
                related_name="showthemes",
                to="planetarium_service.showtheme",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="reservation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium_service.reservation",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="show_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium_service.showsession",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("show_session", "row", "seat")},
        ),
    ]
