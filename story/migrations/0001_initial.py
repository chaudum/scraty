# Generated by Django 3.0.3 on 2020-02-23 18:28

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []  # type: ignore

    operations = [
        migrations.CreateModel(
            name="Story",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.TextField()),
                ("link", models.URLField(blank=True)),
                ("done", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("color", models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("text", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("TODO", "Todo"),
                            ("IN_PROGRESS", "In Progress"),
                            ("VERIFY", "Verify"),
                            ("DONE", "Done"),
                        ],
                        default="TODO",
                        max_length=11,
                    ),
                ),
                (
                    "story",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cards",
                        to="story.Story",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cards",
                        to="story.User",
                    ),
                ),
            ],
        ),
    ]
