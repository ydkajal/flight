# Generated by Django 4.2.11 on 2024-05-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=120)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
