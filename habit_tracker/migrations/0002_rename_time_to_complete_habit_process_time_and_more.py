# Generated by Django 5.1.7 on 2025-03-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="time_to_complete",
            new_name="process_time",
        ),
        migrations.AlterField(
            model_name="habit",
            name="action",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="habit",
            name="place",
            field=models.CharField(max_length=50),
        ),
    ]
