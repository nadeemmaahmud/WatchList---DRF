# Generated by Django 5.1.7 on 2025-03-25 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlistAPI", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="is_watched",
        ),
        migrations.AlterField(
            model_name="watchlist",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="watchlistAPI.watchcategory",
            ),
        ),
    ]
