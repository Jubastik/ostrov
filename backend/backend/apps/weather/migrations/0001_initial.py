# Generated by Django 4.2.4 on 2023-08-12 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("camp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Weather",
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
                ("temperature", models.IntegerField()),
                ("humidity", models.IntegerField()),
                ("pressure", models.IntegerField()),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "camp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="camp.camp"
                    ),
                ),
            ],
        ),
    ]
