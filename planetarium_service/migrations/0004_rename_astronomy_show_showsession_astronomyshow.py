# Generated by Django 5.1 on 2024-08-30 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("planetarium_service", "0003_astronomyshow_showtheme_showtheme_astronomyshow"),
    ]

    operations = [
        migrations.RenameField(
            model_name="showsession",
            old_name="astronomy_show",
            new_name="astronomyshow",
        ),
    ]