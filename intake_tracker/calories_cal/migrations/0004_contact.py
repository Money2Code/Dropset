# Generated by Django 5.1.1 on 2024-10-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "calories_cal",
            "0003_caloriesintake_carbs_goal_caloriesintake_fats_goal_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=12)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("description", models.TextField()),
            ],
        ),
    ]