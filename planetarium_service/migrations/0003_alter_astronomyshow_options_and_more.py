# Generated by Django 5.1 on 2024-09-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planetarium_service", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="astronomyshow",
            options={"ordering": ["title"]},
        ),
        migrations.AlterModelOptions(
            name="showsession",
            options={"ordering": ["-show_time"]},
        ),
        migrations.RenameField(
            model_name="showsession",
            old_name="astronomyshow",
            new_name="astronomy_show",
        ),
        migrations.RemoveField(
            model_name="astronomyshow",
            name="showtheme",
        ),
        migrations.RemoveField(
            model_name="showtheme",
            name="astronomyshow",
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="duration",
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="show_themes",
            field=models.ManyToManyField(
                blank=True, to="planetarium_service.showtheme"
            ),
        ),
    ]
